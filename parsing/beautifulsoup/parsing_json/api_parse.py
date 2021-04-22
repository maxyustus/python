import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()

data = json.load(source)

# print(json.dumps(data, indent=2))

for item in data['list']['resources']:
    name = item['resources']['fields']['name']
    price = item['resources']['fields']['price']
    print(name, price)

print(50 * float(usd_rates['USD/INR']))