import datetime
from config import DRY_RUN

def process_signal(signal):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    price = 2543.00  # Normally you'd get this from API or TradingView payload
    sl = 13
    backtest_success = 93  # Simulated % for example
    decision = "Approved" if backtest_success >= 90 else "Skipped"

    log_line = f"[{now}] Signal: {signal.upper()} | Price: {price} | SL: {sl} pts | Backtest: {backtest_success}% | Decision: {decision} | Mode: {'DRY-RUN' if DRY_RUN else 'LIVE'}"

    # Print to logs
    print(log_line)

    # Save to file (if dry-run enabled)
    if DRY_RUN:
        with open("trade_log.txt", "a") as file:
            file.write(log_line + "\n")
