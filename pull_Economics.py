import fredapi as fred
import pandas as pd
import os


def pull_economics() -> pd.DataFrame:
    FRED_API_KEY = os.getenv("FRED_API_KEY")
    fred_api = fred.Fred(api_key=FRED_API_KEY)
    df = pd.DataFrame()

    #I will be backtesting a maximum of 15 years, so I will pull data from 2010-01-01
    #It will be easier to just pull in all the info I need and then trim it to the last 15 years.
    
    #Interest + Risk Free Rate
    df['10_Year_Treasury'] = pd.DataFrame(fred_api.get_series('DGS10'))
    df['Interest_Rate'] = pd.DataFrame(fred_api.get_series('FEDFUNDS'))

    #Inflation
    df['Consumer_Price_Index'] = pd.DataFrame(fred_api.get_series('CPIAUCNS'))
    df['Producer_Price_Index'] = pd.DataFrame(fred_api.get_series('PPIACO'))

    #GDP
    df['GDP'] = pd.DataFrame(fred_api.get_series('GDP'))

    #Employment
    df['Unemployment'] = pd.DataFrame(fred_api.get_series('UNRATE'))

    #Consumer Confidence
    df['Consumer_Confidence'] = pd.DataFrame(fred_api.get_series('UMCSENT'))

    #Housing
    df['Housing_Index'] = pd.DataFrame(fred_api.get_series('FIXHAI')) #100 means median income families can afford median income homes, <100 means they can't. This is assumes 20% down payment.

    #Industrial Production
    df['Industrail_Production'] = pd.DataFrame(fred_api.get_series('INDPRO'))

    #Commodities Volatility
    df['Oil_Volatility'] = pd.DataFrame(fred_api.get_series('OVXCLS'))
    df['Gold_Volatility'] = pd.DataFrame(fred_api.get_series('GVZCLS'))
    df['Natural_Gas_Volatility'] = pd.DataFrame(fred_api.get_series('VIXCLS'))

    #Currency
    df['Exchange_Rate'] = pd.DataFrame(fred_api.get_series('DEXUSEU'))

    #Total Trade
    df['Retail_Trade'] = pd.DataFrame(fred_api.get_series('RSXFS'))


    df = df[df.index > '2010-01-01']
    
    return df

def write_economics() -> None:
    economics = pull_economics()
    economics.to_csv("Data\Economics\Economics_data.csv")

if __name__ == "__main__":
    write_economics()