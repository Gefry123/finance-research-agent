import pandas as pd


def compute_rsi(df: pd.DataFrame):

    delta = df["Close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()

    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))


def compute_macd(df: pd.DataFrame):

    ema_26 = df["Close"].ewm(span=26, adjust=False).mean()
    ema_12 = df["Close"].ewm(span=12, adjust=False).mean()

    macd = ema_12 - ema_26

    signal_line = macd.ewm(span=9, adjust=False).mean()

    return macd, signal_line


def compute_moving_averages(df: pd.DataFrame):

    ma50 = df["Close"].rolling(50).mean()
    ma200 = df["Close"].rolling(200).mean()

    return {"ma50": ma50.iloc[-1], "ma200": ma200.iloc[-1]}


def flag_signals(df: pd.DataFrame):

    active_signals = []

    rsi = compute_rsi(df)
    macd, signal_line = compute_macd(df)
    moving_averages = compute_moving_averages(df)

    if rsi.iloc[-1] >= 70:
        active_signals.append(f"RSI overbought at {rsi.iloc[-1]}")
    if rsi.iloc[-1] <= 30:
        active_signals.append(f"RSI oversold at {rsi.iloc[-1]}")
    if macd.iloc[-1] > signal_line.iloc[-1]:
        active_signals.append("MACD bullish crossover")
    if moving_averages["ma50"] > moving_averages["ma200"]:
        active_signals.append("golden cross")
    return active_signals
