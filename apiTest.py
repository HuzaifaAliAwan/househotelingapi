import requests

url = 'http://127.0.0.1:5000/predict'

input_data = {
    "Location": "rawalpindi",
    "season": "summer",
    "Attached Bath": 1,
    "Wifi": 1,
    "AC": 0,
    "Parking": 1,
    "public transport accessible": 1,
    "grocery stores": 1,
    "restaurants": 1,
    "Hospital": 0,
    "nearby tourist attractions": 1
}

response = requests.post(url, json=input_data)

# Print response from the server
if response.status_code == 200:
    print("Prediction:", response.json())
else:
    print("Error:", response.json())
