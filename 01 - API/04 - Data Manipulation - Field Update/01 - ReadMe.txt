Title: Product Properties Bulk Updater for RESTful API

Description:
This repository holds a Python script designed to batch update product properties using a RESTful API.
It can be applied to any API endpoint, given that you have the appropriate authentication token.

The Python script executes the following operations:

1. Excel Data Loading:
It loads an Excel workbook ('your_file_name.xlsx') and processes the data from the active sheet.

2. API Endpoint Definition:
It defines the base API endpoint URL.
This should be replaced with the actual API endpoint specific to your use case.

3. Authentication:
It requires an authentication token to interact with the API endpoint.
You need to replace the placeholder with your real token.

4. Product Data Updating:
It iterates through each product (each row in the spreadsheet starting from the second row to skip the header) and creates a PUT request to update the product properties.
The product properties updated are 'product_tags', 'product_category', 'product_shop_color', and 'product_shop_by_style'.
The product_id is assumed to be in column A and the properties to be updated are assumed to be in columns J to M.

5. Response Handling:
After each update request, it verifies if the update was successful.
If successful, it increments a counter and prints out a success message.
If an error occurs, it prints out an error message.

It's important to note that the script assumes a specific format and placement of data in the Excel file.
Ensure your Excel file aligns with these assumptions.
Furthermore, the API endpoint and authentication token in the script are placeholders and need to be replaced with actual values.

Please ensure you adhere to your API provider's usage policies when using this script.
