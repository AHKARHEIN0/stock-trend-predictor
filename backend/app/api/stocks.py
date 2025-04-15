from fastapi import APIRouter, Query
from app.services.stock_fetcher import fetch_stock_data

router = APIRouter()

@router.get("/stock")
def get_stock(symbol: str = Query(...)):
    return fetch_stock_data(symbol)
