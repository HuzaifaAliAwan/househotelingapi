from flask import Flask, request, jsonify
import xgboost as xgb
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load the saved model and encoders
model = xgb.XGBRegressor()
model.load_model('xgboost_model.model')  # Update with your model path

label_encoder_location = joblib.load('./encoders/location_encoder.pkl')  # Replace with your encoder file path
label_encoder_season = joblib.load('./encoders/season_encoder.pkl')  # Replace with your encoder file path



# Define the API route
@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data from the request
    data = request.get_json()

    # Prepare the data: encode categorical features
    location = data['Location']
    season = data['season']
    
    # Encode categorical columns
    encoded_location = label_encoder_location.transform([location])[0]
    encoded_season = label_encoder_season.transform([season])[0]
    
    # Prepare the data for prediction (Assuming other fields are directly usable)
    features = np.array([[ 
        encoded_location,  # Location
        encoded_season,    # Season
        data['Attached Bath'],
        data['Wifi'], 
        data['AC'], 
        data['Parking'], 
        data['public transport accessible'], 
        data['grocery stores'], 
        data['restaurants'], 
        data['Hospital'], 
        data['nearby tourist attractions']  
    ]])

    # Make the prediction
    prediction = model.predict(features)
    
    # Convert the prediction to a standard Python float
    predicted_price = float(prediction[0])

    # Return the prediction as a JSON response
    return jsonify({'predicted_price_per_day': predicted_price})


@app.route('/home', methods=['get'])
def home():
    
    return jsonify("House Hoteling Price Prediction API Working.")


if __name__ == '__main__':
    app.run(debug=True)
