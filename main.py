from src import data_fetcher as df
from src import signals as sig

data_frame_data = df.fetch_price_data("NVDA")

macd, signal_line = sig.compute_macd(data_frame_data)

moving_averages = sig.compute_moving_averages(data_frame_data)

print(sig.flag_signals(data_frame_data))
