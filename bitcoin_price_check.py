import requests

def main():
    url = "https://api.kraken.com/0/public/Ticker?pair=XBTCAD"

    response = requests.get(url)
    data = response.json()

    print(data)

    current_price = float(data["result"]["XXBTZCAD"]["c"][0])
    print(current_price)

if __name__ == "__main__":
   main()