import csv
# Writes analysis results to CSV
class OutputWriter:
    """Writes analysis results to CSV"""
    def __init__(self, output_file):
        self.output_file = output_file
    # Write results to CSV, quoting all fields to handle commas
    def write_results(self, results):
        with open(self.output_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=results[0].keys(),
                quoting=csv.QUOTE_ALL  # quote all fields to handle commas correctly
            )
            writer.writeheader()
            writer.writerows(results)
