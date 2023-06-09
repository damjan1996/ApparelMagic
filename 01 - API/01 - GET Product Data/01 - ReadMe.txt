Title: ApparelMagic Inventory API Client

Description:

This repository contains a Python script that interacts with the ApparelMagic API to fetch product inventory data.
ApparelMagic is a complete inventory management solution for the apparel industry, and this script is specifically designed to work with its API endpoints.

The Python script functions by performing a GET request to the ApparelMagic API's inventory endpoint, retrieving data related to a specific product. Here are the steps the script follows:

1. Define API endpoint:
The script starts by defining the endpoint URL, which should be specific to your ApparelMagic account and the product whose details you wish to fetch.

2. Authentication:
ApparelMagic uses token-based authentication, and the script uses your authentication token and the current timestamp as authentication parameters.
Note that you need to replace the placeholder with your actual authentication token.

3. Request Execution:
The script performs a GET request to the specified API endpoint, appending the authentication parameters to the URL.

4. Response Check:
The script prints the status code and the response content in JSON format, providing details about the specific product.

Please note that while this script is currently set up to fetch data for a specific product, it could easily be expanded to include other API endpoints and functionality. Be aware that all API requests should comply with ApparelMagic's API usage policies.

Remember to replace the placeholders for your business name, product ID, and authentication token before running the script.
