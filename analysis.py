import pandas as pd

def analysis_data():
    df = pd.read_csv("crypto_data.csv")

    # Top 5 cryptocurrencies by market cap
    top_5 = df.nlargest(5, 'market_cap')

    # Average price of top 50 cryptocurrencies
    average_price = df['current_price'].mean()

    # Highest and lowest 24-hour price changes
    highest_vary = df.loc[df['price_change_percentage_24h'].idxmax()]
    lowest_vary = df.loc[df['price_change_percentage_24h'].idxmin()]

    print("\nTop 5 Cryptocurrencies by Market Cap:")
    print(top_5[['name', 'market_cap']])

    print(f"\nAverage Price of Top 50 Cryptocurrencies: ${average_price:.2f}")

    print(f"\nHighest 24-hour Price Change: {highest_vary['name']} ({highest_vary['price_change_percentage_24h']}%)")
    print(f"Lowest 24-hour Price Change: {lowest_vary['name']} ({lowest_vary['price_change_percentage_24h']}%)")

if __name__ == "__main__":
    analysis_data()



