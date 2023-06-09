import requests
import time
import json

# Define the API endpoint
url = 'https://[your_business].app.apparelmagic.com/api/json/inventory/[your_product_id]'

# Authentication parameters
# You must use your actual authentication token and timestamp
token_value = 'your_authentication_token_here'
time_value = str(int(time.time()))

# Define authentication parameters
auth_params = {
    "time": time_value,
    "token": token_value
}

# Append the auth parameters to the URL
url_appendix = f"?time={time_value}&token={token_value}"
entire_url = (url + url_appendix)

# Execute the GET request to fetch product information
response = requests.get(entire_url, headers={'Content-Type': 'application/json'})

# Check the result - print the status code and the response content
print(response.status_code)
print(response.json())
