from fastapi import FastAPI, UploadFile, Form
import pandas as pd
from indicators import add_technical_indicators
from sentiment import get_sentiment_score
from model import predict_signal

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Crypto Bot API is running!"}

@app.post("/predict")
async def predict(file: UploadFile, sentiment_text: str = Form("")):
    df = pd.read_csv(file.file)
    df = add_technical_indicators(df)
    latest = df.iloc[-1]

    sentiment_score = get_sentiment_score(sentiment_text)
    features = [latest["close"], latest["rsi"], latest["macd"], sentiment_score]
    signal, confidence = predict_signal(features)

    return {
        "signal": signal,
        "confidence": round(confidence, 2),
        "sentiment": sentiment_score
    }
