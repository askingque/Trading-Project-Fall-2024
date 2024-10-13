# scripts/data_collection.py
import csv
import yfinance as yf
import pandas as pd
import pickle
from datetime import datetime

# Files to Dump Into
# "TICKER_data.csv" the information of that respective stock
# "last_pulled.csv" measures the day each stock was last pulled

# Call stock data -> NEEDS Start Date -> get start date from last pulled -> get end date from today -> append data to csv file


def last_pulled(ticker) -> datetime: # Gets start date

    # Load our dictionary containing dates
    try:
        with open('Data\Dates_Pulled\last_pulled_Open_Close.pkl', 'rb') as f:
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
    with open('Data\Dates_Pulled\last_pulled_Open_Close.pkl', 'wb') as f:
        pickle.dump(loaded_dict, f)
    f.close()

    return day_pulled


def pull_open_close(ticker) -> pd.DataFrame:
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


def write_open_close(ticker) -> None:
    stock_data = pull_open_close(ticker)
    with open(f"Data\Open_Close\{ticker}_Open_Close_data.csv", mode="w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(stock_data.columns)
        for row in stock_data.itertuples():
            writer.writerow(row)
    file.close()


if __name__ == "__main__":
    write_open_close("MSFT")