import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.services.risk_manager import is_trade_allowed

def test_allowed_trade():
    assert is_trade_allowed(confidence=0.9, trade_amount=5, daily_loss=100) == True

def test_block_low_confidence():
    assert is_trade_allowed(confidence=0.5, trade_amount=5, daily_loss=100) == False

def test_block_large_trade():
    assert is_trade_allowed(confidence=0.9, trade_amount=50, daily_loss=100) == False

def test_block_daily_loss():
    assert is_trade_allowed(confidence=0.9, trade_amount=5, daily_loss=1000) == False
