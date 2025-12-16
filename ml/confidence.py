PATTERN_BONUS = {
    "TIGHT_BASE": 0.12,
    "BREAKOUT_SETUP": 0.10,
    "PULLBACK_CONTINUATION": 0.08,
    "NEAR_52W_HIGH": 0.06,
    "MOMENTUM": 0.04,
}


def compute_confidence(
    ml_prob: float,
    rule_score_norm: float,
    pattern: str,
    volume_support: int,
    rejection: int,
    financial_score: float,
):
    """
    Converts raw ML probability into trader-friendly confidence score (0–1)
    """

    base = (
        0.55 * ml_prob
        + 0.30 * rule_score_norm
        + 0.15 * PATTERN_BONUS.get(pattern, 0)
    )

    # bonus / penalty from financial results
    base += financial_score

    # penalties
    if volume_support == 0:
        base -= 0.05

    if rejection == 1:
        base -= 0.08


    # clamp
    base = max(0.0, min(1.0, base))

    return round(base, 3)
