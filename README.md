## MPG Project

This script calculates the distance between two addresses and updates the result in a Google Sheets document in real-time. It uses the Geoapify API for geocoding and the `pygsheets` library to interact with Google Sheets.

### Requirements

- Python 3.x
- [Geoapify API Key](https://www.geoapify.com/)
- Google Cloud service account credentials for Google Sheets API access

### Installation

1. Clone this repository or download the script.
2. Install the required Python packages:

```bash
pip install pygsheets requests
```

3. Set up Google Sheets API:

Create a Google Cloud project and enable the Google Sheets API.
Create a service account and download the credentials.json file.
Share your Google Sheet with the service account email (found in the credentials.json file).

### Configuration

1. Place your credentials.json file in the same directory as the script.
2. Open the Google Sheet you want to interact with and make sure it has the right worksheet name.
3. Obtain a Geoapify API key and replace the placeholder toner_maps_api_key in the script with your actual API key.

### Usage

The script retrieves two address values from the specified cells in the Google Sheet and calculates the distance between them.

#### Example Use Case:

1. The script retrieves values from cells D2 (start address) and F2 (end address).
2. The calculated distance is then updated in cell G2 of the same sheet.
3. The script runs continuously, updating the sheet every 3 seconds.
Change these values to suit your use case

To run the script:

```bash
python script.py
```

To stop the script, press Ctrl + C.

## Extra

### License
This project is licensed under the MIT License - see the LICENSE.md file for details.

### Acknowledgements
Thanks to the open-source community for various Python libraries that made this simulation possible.