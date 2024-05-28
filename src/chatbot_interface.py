import streamlit as st
from document_conversion import convert_pdf_to_txt, convert_docx_to_txt
from ocr_processing import image_to_text
from llm_integration import extract_entities, summarize_text, classify_text, translate_text, answer_question

def main():
    st.set_page_config(page_title="AI-Powered Document Processing Pipeline", layout="wide")
    
    st.sidebar.title("Navigation")
    options = st.sidebar.radio("Go to", ["Upload Document", "View Extracted Text", "View Entities", "View Summary", "View Classification", "View Translation", "Question and Answer"])
    
    st.markdown("""
    <style>
    .main {
        background-color: #000000;
        color: #ffffff;
    }
    .sidebar .sidebar-content {
        background-color: #333333;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)
    
    if options == "Upload Document":
        st.title("Upload a Document")
        uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "png", "jpg", "jpeg"])
        if uploaded_file is not None:
            file_extension = uploaded_file.name.split('.')[-1]
            filetype = uploaded_file.type
            text = ""
            if file_extension == 'pdf':
                text = convert_pdf_to_txt(uploaded_file)
            elif file_extension == 'docx':
                text = convert_docx_to_txt(uploaded_file)
            elif file_extension in ['png', 'jpg', 'jpeg']:
                text = image_to_text(uploaded_file)
            else:
                st.write("Unsupported file format")
            
            if text:
                st.session_state.text = text
                st.session_state.filename = uploaded_file.name
                st.session_state.filesize = uploaded_file.size
                st.session_state.filetype = filetype
                st.session_state.extension = file_extension
                st.success("Document processed successfully! Use the navigation menu to view different aspects.")
            else:
                st.error("Failed to process the document. Please try again with a different file.")
    
    elif options == "View Extracted Text":
        st.title("Extracted Text")
        if 'text' in st.session_state:
            st.write(st.session_state.text)
        else:
            st.write("No document uploaded. Please upload a document first.")
    
    elif options == "View Entities":
        st.title("Extracted Entities")
        if 'text' in st.session_state:
            entities = extract_entities(st.session_state.text)
            st.write(entities)
        else:
            st.write("No document uploaded. Please upload a document first.")
    
    elif options == "View Summary":
        st.title("Summary")
        if 'text' in st.session_state:
            summary = summarize_text(st.session_state.text)
            st.write(summary)
        else:
            st.write("No document uploaded. Please upload a document first.")
    
    elif options == "View Classification":
        st.title("Classification")
        if 'text' in st.session_state:
            classification_info = classify_text(
                st.session_state.text, 
                st.session_state.filename, 
                st.session_state.filesize, 
                st.session_state.filetype, 
                st.session_state.extension
            )
            st.write(f"Filename: {classification_info['filename']}")
            st.write(f"Filesize: {classification_info['filesize']} bytes")
            st.write(f"Filetype: {classification_info['filetype']}")
            st.write(f"Extension: {classification_info['extension']}")
            st.write(f"Classification: {classification_info['classification']}")
        else:
            st.write("No document uploaded. Please upload a document first.")
    
    elif options == "View Translation":
        st.title("Translation")
        if 'text' in st.session_state:
            translation_fr = translate_text(st.session_state.text, target_language="fr")
            translation_hi = translate_text(st.session_state.text, target_language="hi")
            st.write("Translation to French:")
            st.write(translation_fr)
            st.write("Translation to Hindi:")
            st.write(translation_hi)
        else:
            st.write("No document uploaded. Please upload a document first.")
    
    elif options == "Question and Answer":
        st.title("Question and Answer")
        if 'text' in st.session_state:
            if 'messages' not in st.session_state:
                st.session_state.messages = []
            
            user_input = st.text_input("Ask a question about the document:")
            if user_input:
                st.session_state.messages.append({"user": user_input})
                response = answer_question(user_input, st.session_state.text)
                st.session_state.messages.append({"bot": response})
            
            for message in st.session_state.messages:
                if "user" in message:
                    st.write(f"**You:** {message['user']}")
                if "bot" in message:
                    st.write(f"**Bot:** {message['bot']}")
        else:
            st.write("No document uploaded. Please upload a document first.")

if __name__ == "__main__":
    main()

