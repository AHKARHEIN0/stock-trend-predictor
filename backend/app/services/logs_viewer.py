import json
from pathlib import Path
from datetime import datetime, timezone

LOG_FILE = Path(__file__).resolve().parents[2] / "logs" / "trade_log.json"

def read_logs() -> list:
    if not LOG_FILE.exists():
        return []

    with open(LOG_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def get_today_loss() -> float:
    logs = read_logs()
    today = datetime.now(timezone.utc).date()
    total_loss = 0.0

    for log in logs:
        if (
            log.get("result") == "loss"
            and "timestamp" in log
            and datetime.fromisoformat(log["timestamp"]).date() == today
        ):
            total_loss += log.get("price", 0.0)  # or use "amount" if preferred

    return total_loss
