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

# Gets start date
def last_pulled(ticker): 
    try:
        with open('last_pulled.pkl', 'rb') as f:
            loaded_dict = pickle.load(f)
        f.close()
    except(FileNotFoundError, EOFError):
        loaded_dict = {}


    if ticker in loaded_dict.keys():
        day_pulled = datetime(loaded_dict[ticker])
    else:
        day_pulled = None
    
    loaded_dict[ticker] = datetime.now().strftime("%Y-%m-%d")
    with open('last_pulled.pkl', 'wb') as f:
        pickle.dump(loaded_dict, f)
    f.close()

    return day_pulled


def pull_data_online(ticker):
    stock = yf.Ticker(ticker)
    start_date = last_pulled(ticker)

    if start_date is None:
        # Retrieve the first trade date in epoch time
        first_trade_epoch = stock.info['firstTradeDateEpochUtc']
        # Convert epoch time to a human-readable date
        start_date = datetime.fromtimestamp(first_trade_epoch).strftime('%Y-%m-%d')

    stock_data = yf.download(ticker, start=start_date, end=datetime.now().strftime("%Y-%m-%d"))

    # Save data to csv file
    with open(f"{ticker}_data.csv", mode="w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(stock_data.columns)
        for row in stock_data.itertuples():
            writer.writerow(row)
    file.close()

    print(f"{ticker} data saved.")
    return stock_data


# Example: Collecting Apple stock data
if __name__ == "__main__":
    pull_data_online("AAPL")

    #stock = yf.Ticker("AAPL")
    #df = pd.DataFrame(stock.info)
    #print(df.columns.tolist())