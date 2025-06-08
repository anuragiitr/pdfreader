from dotenv import load_dotenv
load_dotenv()

from utils.pdf_utils import extract_text_from_pdf
from qa_agent import create_qa_chain_from_text

if __name__ == "__main__":
    pdf_file = "sample.pdf"
    text = extract_text_from_pdf(pdf_file)
    
    qa_chain = create_qa_chain_from_text(text)

    while True:
        query = input("\nAsk a question about the PDF (or type 'exit'): ")
        if query.lower() == "exit":
            break
        answer = qa_chain.run(query)
        print("Answer:", answer)