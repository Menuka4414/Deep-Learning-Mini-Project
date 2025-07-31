from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def get_sentiment_score(text):
    score = analyzer.polarity_scores(text)
    return score['compound']

# TEST EXAMPLE
text = "Bitcoin crashes due to regulation."
sentiment = get_sentiment_score(text)
print(f"Sentiment score for: '{text}' → {sentiment}")
