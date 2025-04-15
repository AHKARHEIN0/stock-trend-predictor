import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.services.predictor import predict_action

def test_predict_buy():
    action = predict_action(95, 1_500_000)
    assert action == "buy"

def test_predict_sell():
    action = predict_action(320, 300_000)
    assert action == "sell"

def test_predict_hold():
    action = predict_action(150, 750_000)
    assert action == "hold"
