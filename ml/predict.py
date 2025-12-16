import numpy as np

from ml.confidence import compute_confidence
from ml.model import load_model

from features.indicators import (
    is_uptrend,
    ema_trend_strength
)

from features.patterns import (
    classify_pattern,
    has_rejection_near_resistance
)

from features.liquidity import liquidity_pass
from features.financials import analyze_quarterly_financials

from utils.helpers import (
    has_bullish_candles,
    is_consolidating,
    volume_supports_breakout,
    is_near_resistance,
    compute_resistance
)
from utils.financials_loader import get_quarterly_financials

# Load trained & calibrated model
MODEL = load_model()


def predict_today_probability(df, symbol):
    """
    Returns:
    - ml_probability (float)
    - confidence (float)
    - pattern (str)
    - rule_score (int)
    - financial_label (str)
    """

    # ------------------------
    # 1. BASIC FILTERS
    # ------------------------
    if not liquidity_pass(df):
        return None, None, None, 0, "Neutral"

    # ------------------------
    # 1.5. FINANCIAL ANALYSIS
    # ------------------------
    financials_df = get_quarterly_financials(symbol + ".NS")
    financial_analysis = analyze_quarterly_financials(financials_df)
    financial_label = financial_analysis["financial_label"]
    financial_score = financial_analysis["financial_score"]

    uptrend = is_uptrend(df)
    bullish_candles = has_bullish_candles(df)
    consolidation = is_consolidating(df)
    volume_support = volume_supports_breakout(df)

    resistance = compute_resistance(df)
    near_res = is_near_resistance(df, resistance)

    # ------------------------
    # 2. PATTERN CLASSIFICATION
    # ------------------------
    pattern = classify_pattern(
        df=df,
        uptrend=uptrend,
        bullish_candles=bullish_candles,
        consolidation=consolidation,
        volume_support=volume_support,
        near_res=near_res,
        resistance=resistance
    )

    if pattern is None:
        return None, None, None, 0, financial_label

    # ------------------------
    # 3. RULE SCORE (0–10)
    # ------------------------
    rule_score = 0

    if uptrend:
        rule_score += 2
    if bullish_candles:
        rule_score += 2
    if consolidation:
        rule_score += 2
    if volume_support:
        rule_score += 2
    if near_res:
        rule_score += 2

    rule_score = min(rule_score, 10)

    # ------------------------
    # 4. ML FEATURES (MATCH TRAINING)
    # ------------------------
    features = np.array([
        rule_score / 10,                 # rule_score_norm
        ema_trend_strength(df),           # ema_trend_strength
        int(bullish_candles),             # bullish_candles
        int(consolidation),               # consolidation
        int(volume_support),              # volume_support
        int(near_res),                    # near_resistance
        financial_score,                  # results_score
        0.0                               # future expansion placeholder
    ]).reshape(1, -1)

    # ------------------------
    # 5. ML PROBABILITY
    # ------------------------
    ml_prob = MODEL.predict_proba(features)[0][1]

    # ------------------------
    # 6. CONFIDENCE SHAPING (STEP 6)
    # ------------------------
    rejection = has_rejection_near_resistance(df, resistance)

    confidence = compute_confidence(
        ml_prob=ml_prob,
        rule_score_norm=rule_score / 10,
        pattern=pattern,
        volume_support=int(volume_support),
        rejection=int(rejection),
        financial_score=financial_score
    )

    return float(ml_prob), confidence, pattern, rule_score, financial_label
