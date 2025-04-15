from fastapi import APIRouter, Query
from app.services.stock_fetcher import fetch_stock_data
from app.services.risk_manager import is_trade_allowed
from app.services.predictor import predict_action

router = APIRouter()

@router.get("/stock")
def get_stock(symbol: str = Query(...)):
    return fetch_stock_data(symbol)

@router.get("/predict")
def predict(symbol: str = Query(...)):
    stock_data = fetch_stock_data(symbol)

    if "error" in stock_data:
        return {"symbol": symbol, "error": stock_data["error"]}

    price = stock_data["price"]
    volume = stock_data["volume"]
    confidence = 0.9  # temporary static value, will be dynamic when ML is added
    trade_amount = 5  # pretend 5% of capital is being used
    daily_loss = 100  # pretend you've lost $100 today

    prediction = predict_action(price, volume)
    allowed = is_trade_allowed(confidence, trade_amount, daily_loss)

    return {
        "symbol": symbol.upper(),
        "price": price,
        "volume": volume,
        "prediction": prediction,
        "allowed": allowed
    }

