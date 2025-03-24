import json
import requests

# Load configuration data from config.json
with open('secrets.json', 'r') as config_file:
    config = json.load(config_file)

device_id = config['device_id']
variable_name = config['variable_name']
access_token = config['access_token']

# Construct the API URL
url = f"https://api.particle.io/v1/devices/{device_id}/{variable_name}"

# Use the Authorization header to send the access token
headers = {
    "Authorization": f"Bearer {access_token}"
}

# Make the GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print("Value:", data.get("result"))
else:
    print("Error retrieving variable:", response.status_code, response.text)

