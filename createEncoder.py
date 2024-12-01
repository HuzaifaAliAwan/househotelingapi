from sklearn.preprocessing import LabelEncoder
import joblib
import pandas as pd

# Load your data (assuming it's already cleaned)
data = pd.read_csv('data.csv')

# Initialize the label encoders
label_encoder_location = LabelEncoder()
label_encoder_season = LabelEncoder()

# Fit the encoders on the categorical columns
data['Location'] = label_encoder_location.fit_transform(data['Location'])
data['season'] = label_encoder_season.fit_transform(data['season'])


