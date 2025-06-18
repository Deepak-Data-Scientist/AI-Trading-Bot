def process_signal(signal_str):
    try:
        parts = signal_str.split('|')
        signal = parts[0].upper()
        price = float(parts[1].split('=')[1])
        tp = float(parts[2].split('=')[1])
        sl = float(parts[3].split('=')[1])

        print(f"📥 Received Signal: {signal}")
        print(f"📈 Entry Price: {price}")
        print(f"🎯 Take Profit (TP): {tp}")
        print(f"🛡️ Stop Loss (SL): {sl}")

        # --- Dry Run / Real Trade Logic Here ---
        # if dry_run:
        #     log_trade(signal, price, sl, tp)
        # else:
        #     execute_real_trade(signal, price, sl, tp)

    except Exception as e:
        print(f"❌ Error processing signal: {e}")
