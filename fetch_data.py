import requests
import pandas as pd


# # Here I am using CoinGecko API to get market data for crypto.

API_URL = "https://api.coingecko.com/api/v3/coins/markets"

# Try use collection data type as dictionary to store data in key : value pairs and do not allow duplicates.
dict = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 50,
    "page": 1,
    "sparkline": False
}

# It will fetch data from API and makes a GET request to API_URL with the following parameter from Crypto dictionary

def fetch_crypto_data():
    response = requests.get(API_URL, params=dict)
    if response.status_code == 200:
        return response.json()
    else:
        print("You are getting an error on fetching data")
        return []

def save_data_to_csv(data):
    df = pd.DataFrame(data)[['name', 'symbol', 'current_price', 'market_cap', 'total_volume', 'price_change_percentage_24h']]
    df.to_csv("crypto_data.csv", index=False)

if __name__ == "__main__":
    data = fetch_crypto_data()
    save_data_to_csv(data)
try:
    print("You have fetched data and saved successfully!")
except:
    print("Please check you API_URL or GET request")
finally:
    print("You data will be saved successfully in 'crypto_data.csv'")    

