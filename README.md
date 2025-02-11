                              Cryptocurrency Data Fetching and Analysis
# Project Overview
This project fetches live cryptocurrency data for the top 50 cryptocurrencies using the CoinGecko API, analyzes the data, and updates it in a live Excel sheet every 5 minutes.
The project also includes a script for analyzing key insights, such as the top 5 cryptocurrencies by market capitalization and the highest/lowest percentage price changes in the last 24 hours.

# Features

•	Live Data Fetching: Retrieves real-time cryptocurrency data from the CoinGecko API.
•	Data Storage: Saves the fetched data in CSV and Excel formats.
•	Automated Updates: Updates the Excel sheet every 5 minutes with the latest data.
•	Data Analysis: Identifies key insights such as:
o	Top 5 cryptocurrencies by market capitalization.
o	Average price of the top 50 cryptocurrencies.
o	Highest and lowest 24-hour percentage price changes.

# File Structure

├ fetch_data.py         # Fetches live cryptocurrency data
├ update_excel.py     # Updates the Excel sheet every 5 minutes
├ analyze_data.py     # Performs data analysis
├ crypto_data.csv     # Stores the fetched data in CSV format
├ crypto_data.xlsx    # Stores the live updating data in Excel
├ README.md           # Documentation for the project

# Installation

Prerequisites
•	Python 3.x
•	Required Libraries:
pip install pandas requests schedule openpyxl

# How to Run?

1 Fetch Cryptocurrency Data
Run the following command to fetch the latest cryptocurrency data and save it as crypto_data.csv:
python fetch_data.py
2 Update Excel Sheet
Run the following script to update the Excel file every 5 minutes:
python update_excel.py
3 Perform Data Analysis
To analyze the data and get insights, run:
python analysis.py

# Data Fields

The following fields are fetched and stored:
•	Cryptocurrency Name
•	Symbol
•	Current Price (USD)
•	Market Capitalization
•	24-hour Trading Volume
•	24-hour Price Change (%)

