Data Pull Documentation

pull_Open_Close.py:

    last_pulled()
        Takes in a stock symbol and returns the last date that stock was pulled as well as updates that date.

    pull_open_close()
        Takes in a stock symbol, checks the last date it was checked, and pulls the open and close prices as well as Volume, High, and Low for that stock on that date.

    write_open_close()
        Takes in a stock symbol and the open and close prices, and writes them to a file.

    INPUT -> Ticker Symbol
    OUTPUT -> CSV File containing day-to-day data

    NOTES: I maybe want to transfer how/where this data gets stored, but that is for later. DATE 10/12/24 (M/D/Y)

    NOTES: I would probably need to limit data depending on how far back I need to backtest. (I think I'm currently aiming for 3~7D long trades so around 10 years of backtesting?) DATE 10/12/24 

pull_Financials.py:

    pull_financials():
        Takes in a stock symbol and returns the following data:
            Total Revenue, Gross Profit, Operating Income, Net Income -> Income
            EBITDA, Normalized EBITDA, -> Profitability
            Diluted EPS, Basic EPS, -> Earnings Per Share
            Reconciled Cost Of Revenue, Operating Expense -> Costs
            Interest Expense, Interest Income, Tax Provision -> #Taxes
            Total Unusual Items -> Non-recurring Purchases

    write_financials():
        Takes in a stock symbol, calls pull_financials() and then writes it all to a CSV.

    INPUT -> Ticker Symbol
    OUTPUT -> CSV File containing company finances.

    NOTES: I might want to add a way to keep track of when I make calls to pull the company finances.

pull_Economics.py:

    pull_economics():
        Retrieves Federal Reserve Data
    
    write_economics():
        Calls pull_economics() and then writes it all to a CSV.

    INPUT -> None
    OUTPUT -> CSV File containing Federal Reserve Data

    NOTES: Might want to extend it to international economics.




