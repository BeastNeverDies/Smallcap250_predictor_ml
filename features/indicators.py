import pandas as pd
import numpy as np


# -------------------------
# EMA CORE
# -------------------------
def ema(series, span):
    return series.ewm(span=span, adjust=False).mean()


# -------------------------
# ADD EMA (FLEXIBLE)
# -------------------------
def add_ema(df, period):
    """
    Adds EMA column for given period.
    Example: add_ema(df, 10) -> ema_10
    """

    col = f"ema_{period}"

    if col not in df.columns:
        df[col] = ema(df["close"], period)

    return df


# -------------------------
# ATR CORE
# -------------------------
def atr(df, period=14):
    high = df["high"]
    low = df["low"]
    close = df["close"]

    tr = pd.concat(
        [
            high - low,
            (high - close.shift()).abs(),
            (low - close.shift()).abs(),
        ],
        axis=1,
    ).max(axis=1)

    return tr.rolling(period).mean()


# -------------------------
# ADD ATR
# -------------------------
def add_atr(df, period=14):
    """
    Adds ATR column.
    """

    col = f"atr_{period}"

    if col not in df.columns:
        df[col] = atr(df, period)

    return df


# -------------------------
# TREND LOGIC
# -------------------------
def is_uptrend(df, lookback=20):
    """
    Uptrend definition:
    - EMA(10) > EMA(15)
    - Close above EMA(15)
    """

    if len(df) < lookback:
        return False

    df = add_ema(df, 10)
    df = add_ema(df, 15)

    return (
        df["ema_10"].iloc[-1] > df["ema_15"].iloc[-1]
        and df["close"].iloc[-1] > df["ema_15"].iloc[-1]
    )


# -------------------------
# ML FEATURE
# -------------------------
def ema_trend_strength(df):
    """
    Normalized EMA distance (ML feature).
    """

    if len(df) < 20:
        return 0.0

    df = add_ema(df, 10)
    df = add_ema(df, 15)

    return float(
        (df["ema_10"].iloc[-1] - df["ema_15"].iloc[-1])
        / df["ema_15"].iloc[-1]
    )
