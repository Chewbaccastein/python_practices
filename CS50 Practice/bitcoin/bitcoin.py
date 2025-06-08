import sys
import json
import requests

# API:  cba1777c7606fd938711696f159c9e918af24ed6244103949903cd02d27332e9


try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=cba1777c7606fd938711696f159c9e918af24ed6244103949903cd02d27332e9")
    json_str = response.json()

except requests.RequestException:
    sys.exit("API fail")

try:
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    # else:
    #     for data_usd in json_str["data"]:
    #         dollor = (data_usd["priceUsd"])


    dollor = float(json_str["data"]["priceUsd"])
    usd = float(sys.argv[1]) * dollor
    print(f"${usd:,.4f}")

except ValueError:
    sys.exit("Command-line argument is not a number")



# elif sys.argv[1] != int:
#     sys.exit("Command-line argument is not a number")
# else:
#     usd = int(sys.argv[1]) * data["priceUsd"]
#     usd = float(usd)
#     print(f"${usd:,.4f}")
