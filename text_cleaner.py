import re

def clean_text(text):
    """
    Simple text cleaning function.
    Removes extra spaces, special characters, and normalizes whitespace.
    """
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s,.!?]', '', text)
    return text

if __name__ == "__main__":
    sample = "Hello!!!   This   is   a   test... 123!!!"
    print("Before:", sample)
    print("After:", clean_text(sample))
