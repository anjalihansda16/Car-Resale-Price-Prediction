from flask import Flask, request, render_template
import joblib
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the model and the scaler
model = joblib.load('car_price_model.pkl')  # Load the Random Forest model
scaler = joblib.load('scaler.pkl')  # Load the MinMaxScaler

@app.route('/')
def home():
    return render_template('index.html')  # Your input form page

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve form data and ensure correct data type conversion
        form_data = request.form.to_dict()
        print("Form Data Received:", form_data)  # Debugging line

        # Extract numeric features (all converted to float or int)
        numeric_features = [
            float(form_data['km_driven']),
            float(form_data['mileage']),
            float(form_data['engine']),
            float(form_data['max_power']),
            int(form_data['seats']),
            int(form_data['age'])
        ]

        # Handle categorical features manually and one-hot encode them
        fuel = form_data['fuel']  # Example: Diesel, Petrol, etc.
        seller_type = form_data['seller_type']  # Example: Individual, Dealer
        transmission = form_data['transmission']  # Example: Manual, Automatic
        owner = form_data['owner']  # Example: First, Second Hand

        # One-hot encoding for categorical values
        fuel_encoded = [1, 0, 0] if fuel == "Diesel" else [0, 1, 0] if fuel == "Petrol" else [0, 0, 1]
        seller_type_encoded = [1, 0] if seller_type == "Individual" else [0, 1]
        transmission_encoded = [1, 0] if transmission == "Manual" else [0, 1]
        owner_encoded = [1, 0] if owner == "First" else [0, 1]

        # Combine all features into a single list
        features = numeric_features + fuel_encoded + seller_type_encoded + transmission_encoded + owner_encoded
        user_input = np.array([features])

        # Scale the input using the same scaler used during training
        user_input_scaled = scaler.transform(user_input)

        # Make prediction
        prediction = model.predict(user_input_scaled)
        prediction_original = np.expm1(prediction)  # Inverse log transformation to get the original price

        # Return the prediction result
        return render_template('index.html', prediction_text=f'Predicted Car Price: {prediction_original[0]:.2f}')

    except Exception as e:
        print(f"Error: {e}")
        return render_template('index.html', prediction_text="Error in prediction, please check input values.")

if __name__ == "__main__":
    app.run(debug=True)
