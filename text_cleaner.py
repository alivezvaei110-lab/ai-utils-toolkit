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
# This is a simple text cleaner utility
try:
    # Main logic of the script
    process_data()
except ValueError as e:
    print(f"ValueError encountered: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
