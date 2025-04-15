def predict_action(price: float, volume: int) -> str:
    """
    Simulates a prediction using rule-based logic:
    - Buy if price is low and volume is high
    - Sell if price is high and volume is low
    - Hold otherwise
    """
    if price < 100 and volume > 1_000_000:
        return "buy"
    elif price > 300 and volume < 500_000:
        return "sell"
    else:
        return "hold"
