from app.core.config import settings
from pathlib import Path
from dotenv import set_key
from pathlib import Path

ENV_PATH = Path(__file__).resolve().parents[2] / ".env"


def get_settings():
    return {
        "MAX_DAILY_LOSS": settings.MAX_DAILY_LOSS,
        "MAX_TRADE_PERCENT": settings.MAX_TRADE_PERCENT,
        "MIN_CONFIDENCE": settings.MIN_CONFIDENCE
    }

def update_setting(key: str, value: str):
    set_key(str(ENV_PATH), key, value)
