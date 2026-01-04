from textblob import TextBlob
from langdetect import detect
from deep_translator import GoogleTranslator
from src.core.models import SentimentResult

class SentimentAnalyzer:
    # Analyze the sentiment of the given text
    def analyze(self, text: str) -> SentimentResult:
        try:
            lang = detect(text)
        except:
            lang = "unknown"
        # Translate to English if the text is in Arabic
        if lang == "ar":
            try:
                text_en = GoogleTranslator(source="ar", target="en").translate(text)
            except:
                text_en = text
        else:
            text_en = text
        
        # Perform sentiment analysis using TextBlob
        polarity = TextBlob(text_en).sentiment.polarity
        
        # Determine sentiment label based on polarity score
        if polarity >= 0.2:
            label = "positive"
        elif polarity <= -0.2:
            label = "negative"
        else:
            label = "neutral"

        return SentimentResult(text, polarity, label)
