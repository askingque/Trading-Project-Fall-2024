import yfinance as yf
import pandas as pd

def pull_financials(ticker):
    stock = yf.Ticker(ticker)
    financials = pd.DataFrame(stock.financials)

    financials = financials.transpose() #get date as indexing
    #columns we want
    col = ['Total Revenue', 'Gross Profit', 'Operating Income', 'Net Income', #Income
           'EBITDA', 'Normalized EBITDA', #Profitability
           'Diluted EPS', 'Basic EPS', #Earnings Per Share
           'Reconciled Cost Of Revenue', 'Operating Expense', #Costs
           'Interest Expense', 'Interest Income', 'Tax Provision', #Taxes
           'Total Unusual Items'] #Non-recurring items
    financials = financials[col]
    return financials

def write_financials(ticker):
    print(pull_financials(ticker).index)
    #stock_data = pull_financials(ticker)
    #stock_data.to_csv(f"{ticker}_Financials.csv")
    

if __name__ == "__main__":
    write_financials("MSFT")