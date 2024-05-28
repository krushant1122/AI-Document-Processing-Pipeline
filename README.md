
# AI Document Processing Pipeline

This repository contains the source code and documentation for an AI-powered document processing pipeline. The pipeline supports document conversion, OCR, preprocessing, and integration with various language models for information extraction, classification, translation, and question answering.

## Screenshots
![image](https://github.com/krushant1122/AI-Document-Processing-Pipeline/assets/63834509/3080a14e-c895-4b33-bc3c-772b9b0029f9)
![image](https://github.com/krushant1122/AI-Document-Processing-Pipeline/assets/63834509/7a9361da-8f14-4a1b-9822-1643792f1832)
![image](https://github.com/krushant1122/AI-Document-Processing-Pipeline/assets/63834509/4f8ab1f6-5d09-4fd3-a93f-9c4f2e162226)
![image](https://github.com/krushant1122/AI-Document-Processing-Pipeline/assets/63834509/95bc355f-1508-46d2-9d98-b8606c53c8af)
![image](https://github.com/krushant1122/AI-Document-Processing-Pipeline/assets/63834509/b1c225a4-d229-496d-9b89-a115d2ff5681)



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
