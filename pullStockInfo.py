# scripts/data_collection.py
import csv
import yfinance as yf
import pandas as pd
import pickle
from datetime import datetime
import requests
from bs4 import BeautifulSoup

# Files to Dump Into
# "TICKER_data.csv" the information of that respective stock
# "last_pulled.csv" measures the day each stock was last pulled

# Call stock data -> NEEDS Start Date -> get start date from last pulled -> get end date from today -> append data to csv file


def last_pulled(ticker): # Gets start date

    # Load our dictionary containing dates
    try:
        with open('last_pulled.pkl', 'rb') as f:
            loaded_dict = pickle.load(f)
        f.close()
    except(FileNotFoundError, EOFError):
        loaded_dict = {}

    # Check if the ticker is in the dictionary
    if ticker in loaded_dict.keys():
        day_pulled = loaded_dict[ticker]
    else:
        day_pulled = None

    # Update the dictionary with the current date
    loaded_dict[ticker] = datetime.now().strftime("%Y-%m-%d")

    # Save the dictionary
    with open('last_pulled.pkl', 'wb') as f:
        pickle.dump(loaded_dict, f)
    f.close()

    return day_pulled


def pull_open_close(ticker):
    start_date = last_pulled(ticker)

    if start_date is None:
        stock = yf.Ticker(ticker)
        # Retrieve the first trade date in epoch time
        first_trade_epoch = stock.info['firstTradeDateEpochUtc']
        # Convert epoch time to a human-readable date
        start_date = datetime.fromtimestamp(first_trade_epoch).strftime('%Y-%m-%d')

    open_close_data = yf.download(ticker, start=start_date, end=datetime.now().strftime("%Y-%m-%d"))

    #print(f"{ticker} data saved.")
    return open_close_data

def pull_info(ticker):
    stock = yf.Ticker(ticker)
    return stock.info

def pull_financials(ticker):
    stock = yf.Ticker(ticker)
    financials = stock.financials
    return financials

def process_data(ticker):
    #open_close_data = 
    processed_stock_data = pd.DataFrame(pull_financials(ticker))
    return processed_stock_data


def write_data(ticker):
    stock_data = process_data(ticker)
    with open(f"{ticker}_data.csv", mode="w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(stock_data.columns)
        for row in stock_data.itertuples():
            writer.writerow(row)
    file.close()


# Example: Collecting Apple stock data
if __name__ == "__main__":
    write_data("MSFT")

    #stock = yf.Ticker("AAPL")
    #df = pd.DataFrame(stock.info)
    #print(df.columns.tolist())