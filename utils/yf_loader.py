import yfinance as yf
import pandas as pd


def load_daily_data(symbol, period="2y"):
    """
    Loads daily OHLCV data for NSE stocks using yfinance.
    Expects symbol to already include .NS
    Handles MultiIndex columns safely.
    """

    df = yf.download(
        symbol,
        period=period,
        interval="1d",
        auto_adjust=False,
        group_by="column",
        progress=False,
        threads=False
    )

    if df is None or df.empty:
        return None

    # Handle MultiIndex columns (new yfinance behavior)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df = df.reset_index()

    df.columns = [c.lower() for c in df.columns]

    # Final safety check
    required = {"date", "open", "high", "low", "close", "volume"}
    if not required.issubset(df.columns):
        return None

    return df
