
# AI Document Processing Pipeline

This repository contains the source code and documentation for an AI-powered document processing pipeline. The pipeline supports document conversion, OCR, preprocessing, and integration with various language models for information extraction, classification, translation, and question answering.

## Setup Instructions

### Prerequisites

- Python 3.10
- `pytesseract`
- `pdf2image`
- `transformers`
- `nltk`
- `streamlit`
- `retry`
- `sentencepiece`

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/krushant1122p/ai_document_pipeline.git
   cd ai_document_pipeline
   ```
2. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```
3. Download and install Tesseract OCR from [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract).

### Running the Application

1. Start the Streamlit application:

   ```sh
   streamlit run src/chatbot_interface.py
   ```
2. Open your web browser and navigate to `http://localhost:8501`.

## Instructions for Interacting with the Chatbot

1. **Upload Document:** Upload a PDF, DOCX, PNG, JPG, or JPEG file to start processing.
2. **View Extracted Text:** View the text extracted from the uploaded document.
3. **View Entities:** View the named entities extracted from the document.
4. **View Summary:** View the summary of the document.
5. **View Classification:** View the classification of the document, including filename, size, type, and extension.
6. **View Translation:** View translations of the document text to French and Hindi.
7. **Question and Answer:** Ask questions about the document and get answers based on the content.

## Design Choices and Technologies Used

- **Document Conversion and OCR:** `pdf2image`, `pytesseract`, `python-docx`
- **Preprocessing:** `nltk`
- **Language Models:** Hugging Face `transformers`
- **User Interface:** `streamlit`
- **Error Handling and Retries:** `retry`
