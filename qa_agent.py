import os
from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI embedding and model
embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0)

def create_qa_chain_from_text(text):
    # 1. Split text into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = splitter.split_text(text)

    # 2. Wrap chunks as LangChain Documents
    docs = [Document(page_content=chunk) for chunk in chunks]

    # 3. Create FAISS vectorstore from chunks
    vectorstore = FAISS.from_documents(docs, embedding)

    # 4. Create a retriever
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})

    # 5. Create QA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=False
    )

    return qa_chain
