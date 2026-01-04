 # Emotion_Analyst

**Sentiment Analysis for Arabic and English texts**  
A professional Python project with **Clean Architecture** to analyze emotions from any text source: manual input, TXT files, or CSV files.

---

##  Features

- Supports **Arabic and English text analysis**
- Analyze texts from:
  - Manual input
  - TXT files (one text per line)
  - CSV files (all text columns)
- Text cleaning (removes extra spaces, unnecessary symbols)
- Computes **polarity** and classifies text as:
  - Positive
  - Negative
  - Neutral
- Output:
  - Display results in terminal
  - Save results as CSV
- Interactive **Streamlit GUI**
- Clean Architecture: easy to extend without breaking the code

---

##  Project Structure

Emotion_Analyst/
├── src/
│ ├── main.py # Main entry point
│ ├── core/ # Core logic
│ │ ├── cleaner.py
│ │ ├── analyzer.py
│ │ └── models.py
│ ├── input/ # Input sources
│ │ ├── text_input.py
│ │ ├── txt_reader.py
│ │ └── csv_reader.py
│ └── output/ # Output modules
│ ├── printer.py
│ └── csv_writer.py
├── data/ # Sample files
│ └── sample.csv / sample.txt
├── app.py # Streamlit interactive GUI
└── requirements.txt # Project dependencies

---

##  Installation

1. Clone the repository:

```
git clone https://github.com/mohmedAmir/Emotion_analyst.git
```
```
cd Emotion_Analyst
```

### (Optional) Create a virtual environment:

```
python -m venv venv
```
```
venv\Scripts\activate     # Windows
```
```
source venv/bin/activate  # Linux / Mac
```

Install dependencies:

```
pip install -r requirements.txt
```
Required packages: **textblob**, **pandas**, **langdetect**, **deep-translator**, **streamlit**

#### Download TextBlob corpora:


python -m textblob.download_corpora
# Usage
## 1️- Terminal Version

```
python run.py
```

Choose text source: Manual input / TXT / CSV

Results are displayed in the terminal and saved to results.csv

## 2- Streamlit GUI (Interactive Web App)
```
streamlit run app.py
```
Choose text source: Manual input / TXT / CSV

Results are displayed interactively

Download results as CSV with one click

# Example CSV
csv
Copy code
id,text,comment
1,I love this project,هذا المشروع رائع
2,This is bad,التجربة سيئة جدًا
3,It is okay,عادي
# Results
Polarity: Score from -1 (very negative) to +1 (very positive)

Label: Classification (positive, negative, neutral)

Can be displayed in terminal or downloaded as CSV

# Project Extensions
Upgrade the analyzer to BERT models for Arabic and English

Add support for multiple files in one run

Visualize sentiment statistics in Streamlit

Add unit tests using pytest

# Best Practices
Always use a virtual environment to avoid dependency conflicts

Close CSV files in Excel before running the program

Ensure the files contain actual text to analyze
