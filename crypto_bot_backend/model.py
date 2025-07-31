import joblib

clf = joblib.load("models/model.pkl")
encoder = joblib.load("models/encoder.pkl")

def predict_signal(features):
    prediction = clf.predict([features])[0]
    confidence = clf.predict_proba([features])[0].max()
    return encoder.inverse_transform([prediction])[0], confidence