from textblob import TextBlob

# Analyze sentiment using TextBlob
class SentimentAnalyzer:
    """Analyze sentiment using TextBlob"""
    # Get polarity score and classify sentiment
    def get_sentiment(self, text: str) -> float:
        """Return polarity score (-1 to 1)"""
        return TextBlob(text).sentiment.polarity
    
    # Classify sentiment based on polarity
    def classify_sentiment(self, text: str) -> str:
        """Return Positive / Negative / Neutral"""
        polarity = self.get_sentiment(text)
        if polarity > 0:
            return "Positive"
        elif polarity < 0:
            return "Negative"
        else:
            return "Neutral"
