import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file

class Settings:
    MANUAL_MODE = os.getenv("MANUAL_MODE", "true").lower() == "true"
    MAX_DAILY_LOSS = float(os.getenv("MAX_DAILY_LOSS", "500"))
    MAX_TRADE_PERCENT = float(os.getenv("MAX_TRADE_PERCENT", "10"))
    MIN_CONFIDENCE = float(os.getenv("MIN_CONFIDENCE", "0.8"))

settings = Settings()
