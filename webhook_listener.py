import datetime
import random
from config import DRY_RUN, MAX_SL_POINTS, LOT_SIZE

def simulate_backtest_success():
    # Random success rate between 90%–99%
    return round(random.uniform(90.0, 99.9), 1)

def simulate_price_action_confirmation():
    # Randomly simulate trend confirmation (e.g., swing high/low logic)
    return random.choice([True, True, True, False])  # 75% chance confirmed

def simulate_support_resistance_behavior(signal):
    # Randomly decide if S/R level is likely to break or reverse
    if signal.lower() == "buy":
        return random.choice(["Breaks Resistance", "Reverses at Resistance"])
    else:
        return random.choice(["Breaks Support", "Reverses at Support"])

def simulate_trade_result():
    return random.choice(["Target Hit", "SL Hit"])

def process_signal(signal):
    try:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        signal = signal.lower()

        # Simulated values (mocked in dry-run mode)
        entry_price = round(random.uniform(2500, 2600), 2)
        sl = round(entry_price - MAX_SL_POINTS if signal == "buy" else entry_price + MAX_SL_POINTS, 2)
        tp = round(entry_price + (MAX_SL_POINTS * 2) if signal == "buy" else entry_price - (MAX_SL_POINTS * 2), 2)

        backtest = simulate_backtest_success()
        price_action_ok = simulate_price_action_confirmation()
        sr_decision = simulate_support_resistance_behavior(signal)
        final_decision = "TRADE TAKEN" if backtest >= 94 and price_action_ok and "Breaks" in sr_decision else "SKIPPED"

        result = simulate_trade_result() if final_decision == "TRADE TAKEN" else "N/A"

        log = (
            f"[{now}] Signal: {signal.upper()} | Entry: {entry_price} | SL: {sl} | TP: {tp} | Lot: {LOT_SIZE}\n"
            f"Backtest: {backtest}% | Price Action: {'✅' if price_action_ok else '❌'} | S/R Decision: {sr_decision}\n"
            f"Decision: {final_decision} | Result: {result} | Mode: {'DRY-RUN' if DRY_RUN else 'LIVE'}"
        )

        print(log)

        if DRY_RUN:
            with open("trade_log.txt", "a") as f:
                f.write(log + "\n")

    except Exception as e:
        print(f"❌ Error in process_signal: {e}")

