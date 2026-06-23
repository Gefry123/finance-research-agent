from src import data_fetcher as df
from src import signals as sig
from src import news_fetcher as nf
from src import reporter as rep
import sys


# script_name = sys.argv[0]

# if len(sys.argv) > 1:
#     ticker = sys.argv[1]
# else:
#     ticker = "NVDA"

# data_frame_data = df.fetch_price_data(ticker)

# print(rep.generate_report(ticker, sig.flag_signals(
#     data_frame_data), nf.fetch_news(f"{ticker} stock")))

print(nf.scrape_article(
    'https://www.cbsnews.com/news/tech-stock-selloff-ai-profits-nasdaq-nvidia-alphabet-spacex/'))
