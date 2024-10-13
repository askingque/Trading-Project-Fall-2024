import fredapi as fred
import pandas as pd
import os


def pull_economics() -> pd.DataFrame:
    FRED_API_KEY = os.getenv("FRED_API_KEY")
    fred_api = fred.Fred(api_key=FRED_API_KEY)
    
    # Get the data
    # GDP
    GDP = pd.DataFrame(fred_api.get_series('GDP'))
    return GDP

def write_economics() -> None:
    economics = pull_economics()
    economics.to_csv(f"US_Economics.csv")

if __name__ == "__main__":
    write_economics()