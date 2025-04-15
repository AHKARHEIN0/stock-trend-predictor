import sys
import os

# Add the backend directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.services.stock_fetcher import fetch_stock_data

def test_fetch_valid_stock():
    data = fetch_stock_data("AAPL")
    assert "price" in data
    assert "volume" in data
    assert data["symbol"] == "AAPL"

def test_fetch_invalid_stock():
    data = fetch_stock_data("ZZZZZZ")
    assert "error" in data
