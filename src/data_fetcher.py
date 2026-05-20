import yfinance as yf


def fetch_price_data(ticker_symbol: str):
    dat = yf.Ticker(ticker_symbol)
    return dat.history(period='12mo')
