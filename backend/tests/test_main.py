import sys
import os

# Add the backend directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    data = response.json()
    assert response.status_code == 200
    assert "message" in data
    assert "manual_mode" in data
    assert "max_daily_loss" in data
    assert "confidence" in data

def test_predict_endpoint():
    response = client.get("/predict?symbol=AAPL")
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert data["prediction"] in ["buy", "sell", "hold"]
    assert "allowed" in data
    assert isinstance(data["allowed"], bool)

def test_trade_endpoint():
    response = client.post("/trade?symbol=AAPL")
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert data["prediction"] in ["buy", "sell", "hold"]
    assert "allowed" in data
    assert "message" in data

