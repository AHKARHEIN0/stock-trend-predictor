from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import stocks
from app.core.config import settings
from app.services.scheduler import start_scheduler
from app.api import summary
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(stocks.router)

app.include_router(summary.router)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to Stock Predictor API",
        "manual_mode": settings.MANUAL_MODE,
        "max_daily_loss": settings.MAX_DAILY_LOSS,
        "confidence": settings.MIN_CONFIDENCE
    }

@app.on_event("startup")
def on_startup():
    print("🌟 FastAPI startup event triggered")  # add this
    start_scheduler()

