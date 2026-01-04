import streamlit as st
from src.core.cleaner import TextCleaner
from src.core.analyzer import SentimentAnalyzer
from src.input.csv_reader import read_csv
from src.input.txt_reader import read_txt

st.set_page_config(page_title="Emotion Analyst", layout="wide")

st.title("📝 Emotion Analyzer")
st.markdown("حلل أي نصوص (يدوي، TXT، CSV) مع دعم العربية والإنجليزية")

# ----------------------------
# اختيار مصدر النصوص
# ----------------------------
source = st.radio("اختر مصدر النصوص:", ["Manual Input", "TXT file", "CSV file"])

texts = []

if source == "Manual Input":
    user_input = st.text_area("أدخل النصوص هنا (سطر لكل نص):")
    if user_input:
        texts = [line.strip() for line in user_input.split("\n") if line.strip()]

elif source == "TXT file":
    txt_file = st.file_uploader("اختر ملف TXT", type=["txt"])
    if txt_file:
        with open("temp.txt", "wb") as f:
            f.write(txt_file.getbuffer())
        texts = read_txt("temp.txt")

elif source == "CSV file":
    csv_file = st.file_uploader("اختر ملف CSV", type=["csv"])
    if csv_file:
        with open("temp.csv", "wb") as f:
            f.write(csv_file.getbuffer())
        texts = read_csv("temp.csv")

# ----------------------------
# التحليل
# ----------------------------
if texts:
    cleaner = TextCleaner()
    analyzer = SentimentAnalyzer()

    results = []
    for text in texts:
        cleaned = cleaner.clean(text)
        results.append(analyzer.analyze(cleaned))

    # عرض النتائج
    st.subheader("Results:")
    for res in results:
        st.write(f"**Text:** {res.text}")
        st.write(f"Polarity: {res.polarity:.2f}")
        st.write(f"Label: {res.label}")
        st.markdown("---")

    # تحميل النتائج
    import pandas as pd
    df = pd.DataFrame([{"Text": r.text, "Polarity": r.polarity, "Label": r.label} for r in results])
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download CSV", csv, file_name="results.csv", mime="text/csv")
