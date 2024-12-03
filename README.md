# Car Resale Price Prediction     

## Project Overview
The Chief Technology Officer (CTO) at Cardekho24 has requested the data science team to develop and integrate a car price prediction model into the website. This tool will allow sellers to estimate the price of their cars before listing them, based on various features such as make, model, age, mileage, and condition. The data science team will be responsible for developing the model, preprocessing the data, and ensuring its accuracy. The model will then be integrated into the website through a user-friendly interface, enabling sellers to receive price estimates in real-time. This feature aims to improve the seller experience and drive better engagement on the platform.

## Repository Structure
```
├── static/                 
│   └── styles.css           # CSS file for styling the web interface
├── templates/               
│   └── index.html           # Main HTML file for the web interface
├── app/                     
│   └── app.py               # Main Flask app to serve the model and web interface
├── car_price_prediction/    # Python scripts for data analysis and model building
├── car_price_model.pkl      # Serialized machine learning model for deployment
├── scaler.pkl               # Serialized MinMaxScaler used for scaling features
├── cardekho.csv             # Dataset used for training and testing
├── requirements.txt         # Python dependencies required to run the project
└── README.md                # Project overview and instructions
```
## Model Working Demo

