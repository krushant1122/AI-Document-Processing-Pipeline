from pdfminer.high_level import extract_text as extract_pdf_text
from docx import Document

def convert_pdf_to_txt(file_path):
    try:
        return extract_pdf_text(file_path)
    except Exception as e:
        print(f"Error converting PDF: {e}")
        return ""

def convert_docx_to_txt(file_path):
    try:
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        print(f"Error converting DOCX: {e}")
        return ""

if __name__ == "__main__":
    pdf_text = convert_pdf_to_txt('data/sample.pdf')
    docx_text = convert_docx_to_txt('data/sample.docx')
    print(pdf_text)
    print(docx_text)
