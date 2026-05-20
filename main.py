from src import data_fetcher as df
from src import signals as sig
from src import news_fetcher as nf
from src import reporter as rep

data_frame_data = df.fetch_price_data("NVDA")

print(rep.generate_report("NVDA", sig.flag_signals(
    data_frame_data), nf.fetch_news("NVIDIA stock")))
