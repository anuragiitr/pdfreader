import streamlit as st
from utils.pdf_utils import extract_text_from_pdf
from rag_tools import create_vector_db, load_vector_db, get_query_pdf_tool
from langchain.agents import initialize_agent, AgentType
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import Ollama
import os

st.set_page_config(page_title="PDF Q&A App", layout="wide")
st.title("Ask Questions about Your PDF")

if "agent" not in st.session_state:
    st.session_state.agent = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    with st.spinner("Reading PDF..."):
        text = extract_text_from_pdf(uploaded_file)

    # Split into chunks
    chunks = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100).split_text(text)

    # Embed & store
    db = create_vector_db(chunks)

    # Load as tool
    tool = get_query_pdf_tool(db)

    # Create agent
    llm = Ollama(model="mistral")
    agent = initialize_agent([tool], llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    st.session_state.agent = agent
    st.success("PDF loaded. Ask your questions!")

query = st.text_input("Enter your question")

if query and st.session_state.agent:
    st.session_state.chat_history.append(("User", query))
    with st.spinner("Thinking..."):
        response = st.session_state.agent.run(query)
    st.session_state.chat_history.append(("Bot", response))

for role, msg in st.session_state.chat_history:
    st.markdown(f"**{role}:** {msg}")

