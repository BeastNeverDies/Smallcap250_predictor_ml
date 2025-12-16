import os
import pandas as pd
from datetime import datetime

from ranking.rank_today import rank_today
from charts.generate import generate_charts_for_ranked

# Output folders
os.makedirs("output", exist_ok=True)
os.makedirs("charts", exist_ok=True)

def run_daily():
    today = datetime.now().strftime("%Y-%m-%d")

    print(f"\nRunning daily scan for {today}\n")

    df = rank_today("universe/smallcap_250.csv", top_n=5)

    if df.empty:
        print("No valid setups today.")
        return

    # Save CSV
    csv_path = f"output/top_picks_{today}.csv"
    df.to_csv(csv_path, index=False)
    print(f"Saved CSV: {csv_path}")

    # Generate charts
    generate_charts_for_ranked(df)
    print("Charts generated.")

    # Console summary
    print("\nTOP PICKS TODAY:\n")
    print(df[["rank", "symbol", "confidence", "pattern", "rule_score", "financials"]])


if __name__ == "__main__":
    run_daily()
