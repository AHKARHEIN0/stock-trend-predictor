from fastapi import APIRouter, Query
from app.services.stock_fetcher import fetch_stock_data

router = APIRouter()

@router.get("/stock")
def get_stock(symbol: str = Query(...)):
    return fetch_stock_data(symbol)

from app.services.predictor import predict_action

@router.get("/predict")
def predict(symbol: str = Query(...)):
    stock_data = fetch_stock_data(symbol)

    if "error" in stock_data:
        return {"symbol": symbol, "error": stock_data["error"]}

    action = predict_action(stock_data["price"], stock_data["volume"])
    return {
        "symbol": symbol.upper(),
        "price": stock_data["price"],
        "volume": stock_data["volume"],
        "prediction": action
    }
