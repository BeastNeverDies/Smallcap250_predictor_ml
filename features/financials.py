import pandas as pd

def analyze_quarterly_financials(financials_df):
    """
    Analyzes the quarterly financials to determine if the performance is "Good", "Bad", or "Neutral".

    Args:
        financials_df (pd.DataFrame): DataFrame with quarterly financial data from yfinance.

    Returns:
        dict: A dictionary containing 'financial_label' ("Good", "Bad", "Neutral") and
              'financial_score' (0.1, -0.1, 0).
    """
    result = {
        "financial_label": "Neutral",
        "financial_score": 0.0
    }

    if financials_df is None:
        print("DEBUG: Financials dataframe is None.")
        return result
    if financials_df.empty:
        print("DEBUG: Financials dataframe is empty.")
        return result

    try:
        # yfinance quarterly_financials has the most recent quarter as the first column.
        if len(financials_df.columns) < 2:
            print(f"DEBUG: Not enough quarterly data to compare (columns: {len(financials_df.columns)}).")
            return result
            
        # Get the two most recent quarters
        latest_quarter = financials_df.iloc[:, 0]
        previous_quarter = financials_df.iloc[:, 1]

        # Check for 'Total Revenue'
        if 'Total Revenue' not in latest_quarter.index or 'Total Revenue' not in previous_quarter.index:
            print("DEBUG: 'Total Revenue' not found in financial data.")
            return result

        latest_revenue = latest_quarter['Total Revenue']
        previous_revenue = previous_quarter['Total Revenue']

        if latest_revenue > previous_revenue:
            result["financial_label"] = "Good"
            result["financial_score"] = 0.1
        else:
            result["financial_label"] = "Bad"
            result["financial_score"] = -0.1

    except Exception as e:
        print(f"Could not analyze financial data: {e}")
        # Return neutral if any error occurs
        return {
            "financial_label": "Neutral",
            "financial_score": 0.0
        }

    return result
