import mplfinance as mpf
import pandas as pd


def plot_trade_chart(df, symbol, trade_plan):
    """
    Plots price chart with EMAs, TP/SL, resistance and volume.
    Saves chart as PNG.
    """

    df = df.copy()
    df = df.tail(60)
    df.set_index("date", inplace=True)

    add_plots = []

    # EMA lines
    add_plots.append(mpf.make_addplot(df["ema_10"], color="blue"))
    add_plots.append(mpf.make_addplot(df["ema_15"], color="orange"))

    # TP & SL lines
    add_plots.append(
        mpf.make_addplot(
            [trade_plan["tp1"]] * len(df),
            color="green",
            linestyle="--"
        )
    )
    add_plots.append(
        mpf.make_addplot(
            [trade_plan["tp2"]] * len(df),
            color="green",
            linestyle=":"
        )
    )
    add_plots.append(
        mpf.make_addplot(
            [trade_plan["tp3"]] * len(df),
            color="green",
            linestyle="-."
        )
    )
    add_plots.append(
        mpf.make_addplot(
            [trade_plan["sl"]] * len(df),
            color="red",
            linestyle="--"
        )
    )

    # Resistance (30-day high)
    resistance = df["close"].tail(30).max()
    add_plots.append(
        mpf.make_addplot(
            [resistance] * len(df),
            color="purple",
            linestyle="dashdot"
        )
    )

    mpf.plot(
        df,
        type="candle",
        style="yahoo",
        volume=True,
        addplot=add_plots,
        title=f"{symbol} — Trade Setup",
        savefig=f"charts/{symbol}.png"
    )
