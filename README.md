# Twitter Sentiment Analysis
This project is a **Python** program that performs **sentiment analysis** on tweets.  
The goal of the project is to automatically determine whether a tweet expresses a **positive** or **negative** sentiment.

The program reads tweets from a CSV file and analyzes the text of each tweet using the **TextBlob** library, which is a Python tool for natural language processing (NLP).  
TextBlob calculates a **polarity score** for each tweet, which is a number between -1 and 1:

- **Polarity > 0** indicates a positive sentiment.  
- **Polarity < 0** indicates a negative sentiment.  
- The closer the value is to 1 or -1, the stronger the sentiment.

Based on this analysis, the program assigns each tweet a **sentiment label**: either **Positive** or **Negative**.  
Additionally, it records numerical scores, such as the number of retweets and replies, along with the polarity, in an output CSV file.

This allows you to quickly understand the general mood of a set of tweets and compare how different tweets are perceived by the audience.

---

## Project Structure

Emotion_analyst/
│─ src/
│ ├─ data_loader.py # Loads tweets from CSV
│ ├─ text_cleaner.py # Cleans text (optional)
│ ├─ sentiment_analyzer.py # Performs sentiment analysis using TextBlob
│ ├─ output_writer.py # Writes analysis results to CSV
│ └─ init.py
│
├─ run.py # Main script to run the project
├─ project_twitter_data.csv # Sample tweet data for testing
├─ resulting_data.csv # Output file after analysis
├─ requirements.txt # Project dependencies
└─ README.md # This file

---

## Requirements
```
- Python 3.10 or higher  
- Python packages listed in `requirements.txt`, install using:
```
```
pip install -r requirements.txt
```

# Installation
## Clone this repository:
```
git clone https://github.com/mohmedAmir/Emotion_analyst.git
```
## Navigate into the project folder:

```
cd Emotion_analyst
```
## (Optional) Create and activate a Python virtual environment:

### Windows (PowerShell):

```
python -m venv venv
.\venv\Scripts\Activate.ps1
```
### macOS/Linux:

```
python3 -m venv venv
source venv/bin/activate
```
## Install required libraries:

```
pip install -r requirements.txt
```
# How to Run
Make sure project_twitter_data.csv exists in the project folder, then run:

```
python run.py
```
The output will be saved in resulting_data.csv with the following columns:

Number of Retweets → number of retweets

Number of Replies → number of replies

Polarity → sentiment score (-1 very negative → 1 very positive)

Sentiment → final classification: **Positive or Negative** 

### Notes
Any tweet containing a comma , should be enclosed in double quotes " " in the CSV file.
