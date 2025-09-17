import pygsheets, requests, math, time
 
client = pygsheets.authorize(service_account_file="mpg_project/credentials.json") 
spreadsht = client.open("YOUR_SHEET_NAME") 
worksht = spreadsht.worksheet("title", "YOUR_TAB_NAME") 

NUMBER_OF_CALLS_PER_MINUTE = 10

def calculateDistance(start, end):

    toner_maps_api_key = "YOUR_API_KEY"

    start_address = start
    end_address = end

    start_url = f"https://api.geoapify.com/v1/geocode/search?text={start_address}&limit=1&apiKey={toner_maps_api_key}"
    end_url = f"https://api.geoapify.com/v1/geocode/search?text={end_address}&limit=1&apiKey={toner_maps_api_key}"

    response = requests.get(start_url)

    if response.status_code == 200:

        data = response.json()

        result = data["features"][0]

        start_latitude = result["geometry"]["coordinates"][1]
        start_longitude = result["geometry"]["coordinates"][0]

    else:
        print(f"Request failed with status code {response.status_code}")

    response = requests.get(end_url)

    if response.status_code == 200:

        data = response.json()

        result = data["features"][0]

        end_latitude = result["geometry"]["coordinates"][1]
        end_longitude = result["geometry"]["coordinates"][0]

    else:
        print(f"Request failed with status code {response.status_code}")

    vertical_displacement = end_latitude - start_latitude
    horizontal_displacement = end_longitude - start_longitude

    displacement = math.sqrt((vertical_displacement**2) + (horizontal_displacement**2))

    return f"{displacement*54.6}"

try:
    while True:
        print("Running")

        x = calculateDistance(worksht.get_value("D2"), worksht.get_value("F2"))

        worksht.update_value("G2", x)

        y = calculateDistance(worksht.get_value("D2"), worksht.get_value("J2"))

        worksht.update_value("K2", y)

        time.sleep(60/NUMBER_OF_CALLS_PER_MINUTE)

except KeyboardInterrupt:
    print("\nExiting...")
