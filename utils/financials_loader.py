import yfinance as yf
import pandas as pd

def get_quarterly_financials(symbol):
    """
    Fetches quarterly financial data for a given stock symbol.

    Args:
        symbol (str): The stock symbol to fetch data for.

    Returns:
        pd.DataFrame: A DataFrame containing the quarterly financial data,
                      or None if an error occurs.
    """
    try:
        stock = yf.Ticker(symbol)
        quarterly_financials = stock.quarterly_financials
        return quarterly_financials
    except Exception as e:
        print(f"Error fetching quarterly financials for {symbol}: {e}")
        return None
