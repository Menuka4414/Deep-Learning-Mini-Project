import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
from indicators import add_technical_indicators

df = pd.read_csv("data/price.csv")
df = add_technical_indicators(df)
df["sentiment"] = [-0.5, 0.2, 0.5, 0.7, -0.3]
df["target"] = ["SELL", "HOLD", "BUY", "BUY", "SELL"]

features = df[["close", "rsi", "macd", "sentiment"]]
labels = df["target"]

encoder = LabelEncoder()
y = encoder.fit_transform(labels)

clf = DecisionTreeClassifier()
clf.fit(features, y)

joblib.dump(clf, "models/model.pkl")
joblib.dump(encoder, "models/encoder.pkl")

print("model trained and saved.")