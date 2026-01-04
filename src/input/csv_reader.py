import pandas as pd

def read_csv(file_path: str):
    """
    Read a CSV file and return a list of texts from all text columns.
    """
    try:
        df = pd.read_csv(file_path)
        texts = []

        # Automatically detect text columns (object dtype)
        text_columns = df.select_dtypes(include=['object']).columns.tolist()
        if not text_columns:
            print("No text columns found in the file")
            return []

        print(f"Analyzing the following text columns automatically: {text_columns}")

        for col in text_columns:
            # ignore NaN values and convert to string
            texts.extend(df[col].dropna().astype(str).tolist())

        return texts

    except FileNotFoundError:
        print(f"File {file_path} not found")
        return []
