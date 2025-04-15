from app.core.config import settings

def is_trade_allowed(confidence: float, trade_amount: float, daily_loss: float) -> bool:
    if confidence < settings.MIN_CONFIDENCE:
        return False
    if trade_amount > settings.MAX_TRADE_PERCENT:
        return False
    if daily_loss > settings.MAX_DAILY_LOSS:
        return False
    return True
