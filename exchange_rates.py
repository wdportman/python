import requests
APP_ID = 'ccc6074c3fce44dc95849334716cab0f'
ENDPOINT = 'https://openexchangerates.org/api/latest.json'

response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")
print (response)