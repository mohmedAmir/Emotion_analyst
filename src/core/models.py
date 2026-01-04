from dataclasses import dataclass

@dataclass
class SentimentResult:
    text: str
    polarity: float
    label: str
