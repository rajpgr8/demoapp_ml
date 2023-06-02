import requests
import json

# Define the input data
input_data = {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}

# Convert the input data to JSON format
input_json = json.dumps(input_data)

# Set the URL of the ML model's API endpoint
model_url = "http://iris-model-endpoint.com/predict"

# Send a POST request to the model endpoint with the input data
response = requests.post(model_url, data=input_json)

# Check if the request was successful
if response.status_code == 200:
    # Get the prediction from the response
    prediction = response.json()
    print("Prediction:", prediction)
else:
    print("Error:", response.text)
