from src.data_loader import DataLoader
from src.sentiment_analyzer import SentimentAnalyzer
from src.output_writer import OutputWriter
def main():
    # ==== Files ====
    tweet_file = "project_twitter_data.csv"
    output_file = "resulting_data.csv"

    # ==== Loading Tweets ====
    loader = DataLoader(tweet_file)
    tweets = loader.load_tweets()

    # ==== Analyzing Sentiment ====
    analyzer = SentimentAnalyzer()
    results = []

    for row in tweets:
        text = row["Tweet Text"]  # column name in CSV
        polarity = analyzer.get_sentiment(text)
        sentiment = analyzer.classify_sentiment(text)

        results.append({
            "Number of Retweets": row["Number of Retweets"],
            "Number of Replies": row["Number of Replies"],
            "Polarity": polarity,
            "Sentiment": sentiment
        })

    # ==== Writing the results ====
    writer = OutputWriter(output_file)
    writer.write_results(results)

    print("The data was processed and the results were written in", output_file)
if __name__ == "__main__":
    main()