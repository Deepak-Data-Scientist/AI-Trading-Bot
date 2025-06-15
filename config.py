import os

API_KEY = os.getenv("DELTA_API_KEY")
API_SECRET = os.getenv("DELTA_API_SECRET")
LOT_SIZE = int(os.getenv("LOT_SIZE", 50))
MAX_SL_POINTS = int(os.getenv("MAX_SL_POINTS", 14))
LEVERAGE = int(os.getenv("LEVERAGE", 100))
SIGNAL_THRESHOLD = float(os.getenv("SIGNAL_THRESHOLD", 0.90))
