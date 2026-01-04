from src.core.cleaner import TextCleaner
from src.core.analyzer import SentimentAnalyzer
from src.input.text_input import get_texts_from_user
from src.input.txt_reader import read_txt
from src.input.csv_reader import read_csv
from src.output.printer import print_results
from src.output.csv_writer import save_to_csv

def run():
    cleaner = TextCleaner()
    analyzer = SentimentAnalyzer()

    print("Choose the source of texts:")
    print("1 - Manual input")
    print("2 - TXT file")
    print("3 - CSV file")
    choice = input("Choose 1/2/3: ").strip()
    if choice == "1":
        texts = get_texts_from_user()
    elif choice == "2":
        file_path = input("Enter TXT file path: ").strip()
        texts = read_txt(file_path)
    elif choice == "3":
        file_path = input("Enter CSV file path: ").strip()
        texts = read_csv(file_path)
    else:
        print("Invalid choice")
        return

    results = []
    for text in texts:
        cleaned_text = cleaner.clean(text)
        results.append(analyzer.analyze(cleaned_text))

    print_results(results)
    save_to_csv(results)

if __name__ == "__main__":
    run()
