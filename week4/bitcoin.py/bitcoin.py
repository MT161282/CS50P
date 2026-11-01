import sys

import requests


if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

api_key = "YOUR_COINCAP_API_KEY"

try:
    response = requests.get(
        f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"
    )
    response.raise_for_status()

    bitcoin_price = float(response.json()["data"]["priceUsd"])
except (requests.RequestException, KeyError, ValueError):
    sys.exit("Unable to retrieve Bitcoin price")

total_cost = bitcoins * bitcoin_price

print(f"${total_cost:,.4f}")
