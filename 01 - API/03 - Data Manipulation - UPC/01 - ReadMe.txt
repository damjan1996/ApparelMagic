Title: ApparelMagic API GTIN Updater

Description:
This repository contains a Python script designed to interact with the ApparelMagic API, specifically for updating product GTINs (Global Trade Item Number).
ApparelMagic is a comprehensive inventory management solution for the apparel industry.

The Python script in this repository performs the following steps:

1. Excel Data Loading:
Opens an Excel spreadsheet file ('03 - product_data_upc.xlsx') and loads the product data (SKU IDs and GTINs).

2. API Endpoint Definition:
The script defines the base API endpoint URL specific to your ApparelMagic account's inventory data.

3. Authentication:
The script uses your actual authentication token and the current timestamp for authenticating with the API endpoint.
Replace the placeholder with your real token.

4. Product Data Updating:
The script iterates through each product (row in the spreadsheet) and makes a PUT request to the API to update the GTIN (UPC_DISPLAY) for each product.
The SKU ID is assumed to be in Column A and GTIN in Column S.

5. Response Checking:
After each update request, the script checks if the update was successful.
If it was, it increments a counter and prints out a success message. If not, it prints out an error message.

Note: Ensure to replace all placeholders related to the API endpoint and authentication with your specific details before using the script.
Moreover, the script assumes a specific format and placement of data in the spreadsheet, ensure your Excel file corresponds to it.

Please follow ApparelMagic's API usage policies while making use of this script.
