def read_txt(file_path: str):

   #read a text file and return a list of non-empty lines
    
    texts = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():  # ignore empty lines
                    texts.append(line.strip())
    except FileNotFoundError:
        print(f"File {file_path} not found")
    return texts
