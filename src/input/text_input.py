


def get_texts_from_user():
    print("Enter text (type 'exit' to finish):")
    texts = []

    while True:
        text = input("> ")
        if text.lower() == "exit":
            break
        if text.strip():
            texts.append(text)

    return texts
