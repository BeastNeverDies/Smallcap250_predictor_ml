from utils.yf_loader import load_daily_data
from features.indicators import add_ema, add_atr
from charts.plot import plot_trade_chart


def generate_charts_for_ranked(df_ranked):
    """
    Generates charts for ranked trade setups.
    """

    for _, row in df_ranked.iterrows():
        symbol = row["symbol"]
        print(f"Generating chart for {symbol}...")

        df = load_daily_data(symbol)
        if df is None:
            continue

        df = add_ema(df, 10)
        df = add_ema(df, 15)
        df = add_atr(df, 14)

        trade_plan = {
            "tp1": row["tp1"],
            "tp2": row["tp2"],
            "tp3": row["tp3"],
            "sl": row["sl"],
        }

        plot_trade_chart(df, symbol, trade_plan)
