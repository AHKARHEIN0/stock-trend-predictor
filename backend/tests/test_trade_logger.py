import sys, os, json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.services.trade_logger import log_trade, LOG_FILE

def test_log_trade():
    sample = {
        "symbol": "AAPL",
        "prediction": "buy",
        "allowed": True,
        "confidence": 0.92,
        "price": 180.50
    }

    log_trade(sample)
    assert LOG_FILE.exists()

    data = json.loads(LOG_FILE.read_text())
    assert isinstance(data, list)
    assert any(entry["symbol"] == "AAPL" for entry in data)
