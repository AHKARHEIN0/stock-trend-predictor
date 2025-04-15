from fastapi import FastAPI
from app.api import stocks
from app.core.config import settings

app = FastAPI()
app.include_router(stocks.router)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to Stock Predictor API",
        "manual_mode": settings.MANUAL_MODE,
        "max_daily_loss": settings.MAX_DAILY_LOSS,
        "confidence": settings.MIN_CONFIDENCE
    }
