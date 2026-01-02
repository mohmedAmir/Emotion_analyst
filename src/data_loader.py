import csv

# Loads tweets from a CSV file
class DataLoader:
    """Loads tweets from a CSV file"""
    def __init__(self, tweet_file):
        self.tweet_file = tweet_file

    def load_tweets(self):
        """Load tweets from CSV, handle commas in text correctly"""
        with open(self.tweet_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f, quotechar='"')  # use quotechar to handle commas in text
            return list(reader)
