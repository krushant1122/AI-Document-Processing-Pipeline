import re
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk

nltk.download('punkt')

def preprocess_text(text):
    try:
        text = re.sub(r'\s+', ' ', text)  # Remove extra whitespace
        sentences = sent_tokenize(text)  # Sentence segmentation
        tokens = [word_tokenize(sentence) for sentence in sentences]  # Tokenization
        return tokens
    except Exception as e:
        print(f"Error preprocessing text: {e}")
        return []

# Example usage
if __name__ == "__main__":
    text = "This is an example text. It will be processed."
    preprocessed_text = preprocess_text(text)
    print(preprocessed_text)
