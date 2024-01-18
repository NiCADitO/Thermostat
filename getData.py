import json
import requests

#Used to print data
access_token = """ACCESS_TOKEN_GOES_HERE"""


url = "https://api.ecobee.com/1/thermostat"
headers = {
    "Content-Type": "text/json",
    "Authorization": f"Bearer {access_token}"
}

data = {
    "selection": {
        "selectionType": "registered",
        "selectionMatch": "",
        "includeRuntime": True
    }
}

response = requests.get(url, headers=headers, params={"format": "json", "body": json.dumps(data)})
thermostat_data = response.json()
print(thermostat_data)