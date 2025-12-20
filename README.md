# 🚀 Smallcap-250 Smart Trade Scanner (India)

A **rule-driven + ML-assisted stock scanner** for the **NIFTY Smallcap 250**, supercharged with **Institutional-Grade Indicators**. Designed for **short-term swing trades (1–5 days)** with strict risk management.

---

## 🔍 What This Project Does

Every trading day **after market close**, the system:

1.  **Traffic Light System:** Checks if **NIFTY 50** is Bullish. If Bearish, strict filters activate.
2.  **Smart Filtering:**
    *   **Relative Strength (RS):** Finds stocks outperforming Nifty.
    *   **ADX > 25:** Ensures strong trend momentum.
    *   **VCP:** Detects volatility contraction (calm before the storm).
    *   **Weekly Trend:** Confirms alignment with the bigger picture.
3.  **Financial Health:** Scores growth on a **0.0–1.0 Scale** (Green = Good, Red = Bad).
4.  **Prediction:** Uses ML + Rule Logic to predict 5-day upside.
5.  **Output:** Generates a **Color-Coded Dashboard** of Top 5 Picks.

---

## 📊 Trade Style

| Parameter | Value |
|--------|------|
| Market | NSE 🇮🇳 |
| Universe | NIFTY Smallcap 250 |
| Timeframe | Daily + Weekly Alignment |
| Holding Period | 1–5 days |
| Target Range | 5% – 20% |
| Stop Loss | ATR-Based Trailing Stop |

---

## 🧠 Smart Features

- � **Market Regime Filter:** "Red Light" if Market is Bearish (Nifty < 50EMA).
- 📈 **Relative Strength:** We only buy leaders, not laggards.
- ⚡ **ADX Power:** Filters out weak, drifting trends.
- 📉 **Volatility Contraction (VCP):** Catches explosive moves early.
- 💰 **Numeric Financials:** 
    - `> 0.50`: Positive Growth
    - `< 0.50`: Negative Growth
    - `0.00 – 1.00`: Color-coded score.

---

## 🤖 Machine Learning (Used Carefully)

- Model: **Calibrated Logistic Regression**
- Label: *Did the stock move X% within 5 trading days?*
- **Final Confidence** = Rule Score (Patterns/Indicators) + ML Probability + Financial Score.

---

## 📈 Sample Output

The console now prints a beautiful color-coded table:

```text
RANK | SYMBOL        | CONFIDENCE | PATTERN               | RULE_SCORE | FINANCIALS | TRAILING_SL
---------------------------------------------------------------------------------------------
1    | HINDCOPPER.NS | 0.85       | BREAKOUT_SETUP        | 9          | 0.95 (Grn) | 362.80
2    | GRANULES.NS   | 0.78       | MOMENTUM              | 8          | 0.88 (Grn) | 415.50
3    | MANAPPURAM.NS | 0.65       | PULLBACK_CONTINUATION | 7          | 0.60 (Yel) | 180.20
```

---

## 📂 Project Structure

```text
├── backtesting/           # Simple backtesting engine
├── data/                  # Historical stock data storage
├── features/              # Feature Engineering (ADX, RSI, VCP, etc.)
├── models/                # Trained ML models
├── output/                # Daily CSV logs
├── ranking/               # Ranking & Trade Plan Logic
├── run_daily.py           # Main execution script
└── utils/                 # Helper functions
```

---

## ▶️ How To Run

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Scanner:**
   ```bash
   python run_daily.py
   ```

3. **Backtest a Stock:**
   ```bash
   python -m backtesting.simple_backtest
   ```

## ⚠️ Disclaimer

This project is built for **educational and research purposes only**.  
It is **not financial advice**. Trading involves significant risk. Consult a **SEBI-registered advisor**.

**Built with ❤️ using price action, discipline, and data.**
