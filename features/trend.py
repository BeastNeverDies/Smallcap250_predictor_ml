def in_uptrend(df):
    """
    Checks if stock is in short-term uptrend based on EMA alignment.
    """

    if df is None or len(df) < 20:
        return False

    latest = df.iloc[-1]

    if latest["close"] <= latest["ema_10"]:
        return False

    if latest["close"] <= latest["ema_15"]:
        return False

    if latest["ema_10"] < latest["ema_15"]:
        return False

    return True
