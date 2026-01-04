import re

class TextCleaner:
    def __init__(self, remove_numbers=True):
        self.remove_numbers = remove_numbers

    def clean(self, text: str) -> str:
        text = text.lower()
        text = re.sub(r"\s+", " ", text)

        if self.remove_numbers:
            text = re.sub(r"\d+", "", text)

        text = re.sub(r"[^\w\s]", "", text)
        return text.strip()
