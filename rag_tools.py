from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.tools import Tool
from langchain.llms import Ollama

# Load embedding model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def create_vector_db(chunks, persist_path="vector_store/faiss_index"):
    db = FAISS.from_texts(chunks, embedding=embedding_model)
    db.save_local(persist_path)
    return db

def load_vector_db(persist_path="vector_store/faiss_index"):
    return FAISS.load_local(persist_path, embeddings=embedding_model)

def get_query_pdf_tool(db):
    retriever = db.as_retriever()

    def query_pdf_db(query: str) -> str:
        docs = retriever.get_relevant_documents(query)
        context = "\n\n".join([doc.page_content for doc in docs])
        prompt = f"Answer the following based on the context:\n\nContext:\n{context}\n\nQuestion:\n{query}"
        llm = Ollama(model="mistral")
        return llm.invoke(prompt)

    return Tool(
        name="QueryPDFDatabase",
        func=query_pdf_db,
        description="Useful for answering questions about the uploaded PDF content."
    )
