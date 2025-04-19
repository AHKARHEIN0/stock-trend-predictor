from fastapi import APIRouter
from app.services.logs_viewer import read_logs

router = APIRouter()

@router.get("/summary")
def get_summary():
    logs = read_logs()
    total = 0
    for log in logs:
        if log.get("allowed") and log.get("result") in ("win", "loss"):
            trade_amount = float(log["price"]) * 0.1  # 💰 simulate 10% trade
            total += trade_amount if log["result"] == "win" else -trade_amount

    return {"net_profit_loss": round(total, 2)}
