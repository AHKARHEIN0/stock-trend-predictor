import json
from pathlib import Path

LOG_FILE = Path("backend/logs/trade_log.json")

def read_logs() -> list:
    if not LOG_FILE.exists():
        return []

    with open(LOG_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
