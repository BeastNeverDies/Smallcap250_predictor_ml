def liquidity_pass(df, min_avg_volume=1_000_000, lookback=20):
    """
    Core liquidity filter:
    - Average volume over last N days must exceed threshold
    """

    if df is None or len(df) < lookback:
        return False

    avg_volume = df["volume"].tail(lookback).mean()

    return avg_volume >= min_avg_volume


# --------------------------------------------------
# Backward-compatible alias (DO NOT REMOVE)
# --------------------------------------------------
def passes_liquidity_filter(df, min_avg_volume=1_000_000, lookback=20):
    """
    Alias for liquidity_pass (kept for compatibility)
    """
    return liquidity_pass(df, min_avg_volume, lookback)
