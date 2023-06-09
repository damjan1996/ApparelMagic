import requests
import time
import pandas as pd

# Define the API endpoint
url = 'https://[your_business].app.apparelmagic.com/api/json/inventory'

# Authentication parameters
# You must use your actual authentication token and timestamp
token_value = 'your_authentication_token_here'
time_value = str(int(time.time()))

# Define authentication parameters
auth_params = {
    "time": time_value,
    "token": token_value
}

# Define the filters to be applied in the API request
filter_field_first = "your_filter_field_1"
filter_operator_first = "="
filter_value_first = "0"
filter_field_second = "your_filter_field_2"
filter_operator_second = "="
filter_value_second = "your_filter_value_2"

# Append the auth parameters and filters to the URL
url_appendix = f"?time={time_value}&token={token_value}&parameters[0][field]={filter_field_first}&parameters[0][operator]={filter_operator_first}&parameters[0][value]={filter_value_first}&parameters[1][field]={filter_field_second}&parameters[1][operator]={filter_operator_second}&parameters[1][value]={filter_value_second}"
entire_url = (url + url_appendix)

# Send GET request to the API
response = requests.get(entire_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse response text into JSON format
    data = response.json()
    product_data = data["response"]

    # Create a DataFrame from the product data
    df = pd.DataFrame(product_data)

    # Export product data to an Excel spreadsheet
    writer = pd.ExcelWriter('product_list.xlsx', engine='xlsxwriter')
    df.to_excel(writer, index=False)
    writer.close()

    # Export the same product data to a second Excel spreadsheet
    writer = pd.ExcelWriter('product_list_edited.xlsx', engine='xlsxwriter')
    df.to_excel(writer, index=False)
    writer.close()

    print("Successfully exported data to the Excel spreadsheets.")
else:
    print(response.text)
    print("Error retrieving data. Status code:", response.status_code)
