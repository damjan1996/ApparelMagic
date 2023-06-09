Title: ApparelMagic API Inventory Data Fetcher and Excel Exporter

Description:
This repository holds a Python script tailored to interact with the ApparelMagic API, specifically designed to fetch inventory data based on certain filters, and export the fetched data into Excel spreadsheets.
ApparelMagic is a comprehensive inventory management solution for the apparel industry.

The Python script provided within this repository performs the following operations:

1. API Endpoint Definition:
It starts with defining the endpoint URL, which is specific to your ApparelMagic account's inventory data.

2. Authentication:
The script uses your actual authentication token and the current timestamp to authenticate with the API endpoint.
Make sure to replace the placeholders with your real token.

3. Filter Parameters:
This script allows you to apply filters to your API request to get a subset of inventory data.
Two filters are defined in the script, replace the placeholders with your desired field, operator, and value for each filter.

4. GET Request:
The script performs a GET request on the API endpoint using the provided filters and authentication parameters.

5. Response Parsing:
It checks the response of the GET request.
If successful, the response is parsed into JSON format and the product data is extracted.

6. Dataframe Creation and Export:
The product data is then transformed into a pandas DataFrame, which is exported into two Excel spreadsheets.

Ensure to replace all placeholders related to the API endpoint, authentication, and filters with your specific details before using the script.

Please follow ApparelMagic's API usage policies while making use of this script.
