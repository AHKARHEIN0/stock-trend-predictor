from apscheduler.schedulers.background import BackgroundScheduler
from app.services.trader import simulate_trade_for_symbols

# ✅ create the scheduler instance here so it's visible to the function
scheduler = BackgroundScheduler()

def start_scheduler():
    print("🔁 start_scheduler() called")

    scheduler.add_job(
        func=lambda: simulate_trade_for_symbols(["AAPL", "TSLA", "MSFT"]),
        trigger="interval",
        seconds=15,  # for testing
        id="auto_trade_job",
        replace_existing=True
    )

    scheduler.start()
    print("✅ APScheduler started.")
