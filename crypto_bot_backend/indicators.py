import pandas as pd
import ta

def add_technical_indicators(df):
    df['rsi'] = ta.momentum.RSIIndicator(df['close']).rsi()
    df['macd'] = ta.trend.MACD(df['close']).macd()
    df = df.fillna(0)
    return df