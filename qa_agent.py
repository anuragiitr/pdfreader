from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama  # Local LLM

def create_qa_chain_from_text(text: str):
    # Step 1: Split document
    docs = [Document(page_content=text)]
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(docs)

    # Step 2: Create embeddings
    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embedding)

    # Step 3: Setup retriever + local LLM (Ollama)
    retriever = vectorstore.as_retriever()
    llm = Ollama(model="mistral")  # or "llama2", "llama3", "gemma", etc.
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    return qa_chain

