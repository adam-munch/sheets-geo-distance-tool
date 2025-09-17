import pygsheets 

# Get all connected spreadsheets

client = pygsheets.authorize(service_account_file="mpg_project/credentials.json") 
print(client.spreadsheet_titles()) 


# Delete a spreadsheet
"""
spreadsht = client.open("YOUR_SPREADSHEET_NAME")
spreadsht.delete()
"""