from transformers import pipeline
from retry import retry

# Define maximum lengths for models
MAX_SUMMARY_LENGTH = 1024
MAX_CLASSIFICATION_LENGTH = 512
MAX_TRANSLATION_LENGTH = 512

@retry(tries=3, delay=2)
def get_ner_model():
    return pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

@retry(tries=3, delay=2)
def get_summarizer():
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

@retry(tries=3, delay=2)
def get_classifier():
    return pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

@retry(tries=3, delay=2)
def get_translator():
    return pipeline("translation", model="Helsinki-NLP/opus-mt-en-hi")

@retry(tries=3, delay=2)
def get_qa_model():
    return pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Named Entity Recognition (NER)
ner_model = get_ner_model()

def extract_entities(text):
    try:
        return ner_model(text)
    except Exception as e:
        print(f"Error extracting entities: {e}")
        return []

# Summarization
summarizer = get_summarizer()

def summarize_text(text):
    try:
        if len(text) > MAX_SUMMARY_LENGTH:
            text = text[:MAX_SUMMARY_LENGTH]
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
        return summary
    except Exception as e:
        print(f"Error summarizing text: {e}")
        return []

# Document Classification
classifier = get_classifier()

def classify_text(text, filename=None, filesize=None, filetype=None, extension=None):
    try:
        if len(text) > MAX_CLASSIFICATION_LENGTH:
            text = text[:MAX_CLASSIFICATION_LENGTH]
        classification = classifier(text)
        document_info = {
            "filename": filename,
            "filesize": filesize,
            "filetype": filetype,
            "extension": extension,
            "classification": classification
        }
        return document_info
    except Exception as e:
        print(f"Error classifying text: {e}")
        return {
            "filename": filename,
            "filesize": filesize,
            "filetype": filetype,
            "extension": extension,
            "classification": []
        }

# Translation
translator = get_translator()

def translate_text(text, target_language="fr"):
    try:
        if target_language == "hi":
            model = "Helsinki-NLP/opus-mt-en-hi"
        else:
            model = "t5-base"
        translator = pipeline("translation", model=model)
        
        if len(text) > MAX_TRANSLATION_LENGTH:
            text = text[:MAX_TRANSLATION_LENGTH]
        translation = translator(text)
        return translation
    except Exception as e:
        print(f"Error translating text: {e}")
        return []

# Question Answering
qa_model = get_qa_model()

def answer_question(question, context):
    try:
        answer = qa_model(question=question, context=context)
        return answer['answer']
    except Exception as e:
        print(f"Error answering question: {e}")
        return "Sorry, I couldn't find an answer."

if __name__ == "__main__":
    text = "This is an example text for testing the models."
    entities = extract_entities(text)
    summary = summarize_text(text)
    classification = classify_text(text, "example.txt", 1024, "text/plain", "txt")
    translation_fr = translate_text(text, target_language="fr")
    translation_hi = translate_text(text, target_language="hi")
    answer = answer_question("What is this text about?", text)
    
    print("Entities:", entities)
    print("Summary:", summary)
    print("Classification:", classification)
    print("Translation to French:", translation_fr)
    print("Translation to Hindi:", translation_hi)
    print("Answer to Question:", answer)
