import pandas as pd
import schedule
import time

from fetch_data import fetch_crypto_data

EXCEL_FILE = "crypto_data.xlsx"

def update_excel():
    data = fetch_crypto_data()
    if data:
        df = pd.DataFrame(data)[['name', 'symbol', 'current_price', 'market_cap', 'total_volume', 'price_change_percentage_24h']]
        with pd.ExcelWriter(EXCEL_FILE, mode="w", engine="openpyxl") as writer:
            df.to_excel(writer, sheet_name="Cryptocurrency Data", index=False)

        print("Your Excel Sheet has been updated!")
        
        user = input("Is your Excel Sheet updated ?\n")
    if user != "":  # Check if the string is NOT empty
         print("Thank you!, You can check you Excel Sheet in your MS Office") # Or whatever you want to do.
    else:
         print("Please update the Excel sheet and enter 'yes' or 'no'.") #Ask again

# Or, if you want to loop until they provide input:

    while user == "":
      user = input("Is your Excel Sheet updated ?\n")
    print("Okay, you can proceed...")

# Continuously updating the data every 5 minutes

schedule.every(5).minutes.do(update_excel)

if __name__ == "__main__":
    update_excel()  # I am implementing Initial update
    while True:
        schedule.run_pending()
        time.sleep(60)  # Try to Wait for 1 minute before checking again


