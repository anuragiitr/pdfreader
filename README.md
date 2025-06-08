Here's an updated, more descriptive `README.md` based on your latest changes — including local model usage, Streamlit integration, and Phase 1 & 2 milestones:

---

````markdown
# 📄 PDF Insights Agent

A local LLM-powered application to extract insights and answer questions from PDF documents.  
Built using `LangChain`, `FAISS`, `pdfplumber`, `SentenceTransformers`, and `Streamlit`.  
Uses **Mistral** via **Ollama** — no external API keys needed.

---

## 🔍 Key Features

- ✅ Extracts text from any PDF using `pdfplumber`
- ✅ Splits text into context-aware chunks
- ✅ Embeds text locally using `all-MiniLM-L6-v2` from `sentence-transformers`
- ✅ Stores and queries text chunks using `FAISS`
- ✅ LLM Agent (via LangChain) answers user questions over the PDF content
- ✅ Streamlit interface to upload PDFs and ask questions interactively

---

## 🛠️ Setup

### Prerequisites

- Python 3.10+
- Ollama installed and Mistral model pulled:
  ```bash
  brew install ollama       # or from https://ollama.com/download
  ollama pull mistral
````

### Install Python dependencies

```bash
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

---

## 🚀 Run the App

### Streamlit App

```bash
streamlit run app.py
```

Then open: [http://localhost:8501](http://localhost:8501)
Upload a PDF and start asking questions!

---

## 🧠 How It Works

### ✅ Phase 1: Basic Pipeline

1. **PDF Upload & Extraction**

   * Extracts all text using `pdfplumber`
2. **Text Chunking**

   * Splits into overlapping chunks using LangChain’s `RecursiveCharacterTextSplitter`
3. **QA Chain**

   * Directly passes chunks into an LLM via LangChain for answering (no memory)

### ✅ Phase 2: RAG with Vector DB

1. **Embeddings**

   * Text chunks are embedded using `sentence-transformers`
2. **Vector Storage**

   * Stored in `FAISS` for similarity search
3. **Agent Tool**

   * LangChain agent uses tool named `QueryPDFDatabase` to search and synthesize answers

---

## 🧪 Example Questions

* "Summarize key findings from the document"
* "What are the issues highlighted in Q2?"
* "List the drivers of revenue decline"

---

## 📁 Repo Structure

```
PDFReader/
├── app.py                  # Streamlit frontend
├── main.py                 # CLI entry (optional)
├── qa_agent.py             # LangChain agent logic
├── pdf_extractor.py        # PDF text extraction
├── vector_store/           # FAISS DB and embeddings
├── requirements.txt
└── README.md
```

---

## 🤖 Model

* 💡 Uses [Mistral](https://ollama.com/library/mistral) (via Ollama) for all LLM queries
* No OpenAI API keys or cloud dependencies required

---

## 📌 Roadmap

* [x] Phase 1: Basic Q\&A with LangChain agent
* [x] Phase 2: Embedding-based Retrieval + Answer generation (RAG)
* [ ] Phase 3: Chat memory for multi-turn conversations
* [ ] Phase 4: Multi-PDF or folder-based support
* [ ] Phase 5: Deployment on HuggingFace/Streamlit Cloud or Docker

---

## 🙌 Credits

* Built using [LangChain](https://www.langchain.com/), [FAISS](https://github.com/facebookresearch/faiss), [SentenceTransformers](https://www.sbert.net/)
* Local LLM via [Ollama](https://ollama.com/)

---

## ⚠️ Note

This is a local-first project: no data leaves your system.

```

---

Let me know if you’d like to break it into shorter sections or add badges, images, or demo GIFs!
```
