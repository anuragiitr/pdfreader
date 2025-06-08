import streamlit as st
from pdf_extractor import extract_text_from_pdf
from qa_agent import create_qa_chain_from_text

st.set_page_config(page_title="PDF Q&A App", layout="wide")

st.title("📄 Ask Questions about Your PDF")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    with st.spinner("Reading PDF..."):
        text = extract_text_from_pdf(uploaded_file)

    qa_chain = create_qa_chain_from_text(text)

    st.success("PDF loaded. You can now ask questions!")

    query = st.text_input("Enter your question")

    if query:
        with st.spinner("Thinking..."):
            answer = qa_chain.run(query)
        st.markdown("### Answer:")
        st.write(answer)
