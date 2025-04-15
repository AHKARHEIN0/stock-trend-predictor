from fastapi import FastAPI
from app.api import stocks
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(stocks.router)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to Stock Predictor API",
        "manual_mode": settings.MANUAL_MODE,
        "max_daily_loss": settings.MAX_DAILY_LOSS,
        "confidence": settings.MIN_CONFIDENCE
    }
