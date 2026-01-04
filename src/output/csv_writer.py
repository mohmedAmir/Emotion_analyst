import csv

def save_to_csv(results, filename="results.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["text", "polarity", "label"])

        for r in results:
            writer.writerow([r.text, r.polarity, r.label])
