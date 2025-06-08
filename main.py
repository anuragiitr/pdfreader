from dotenv import load_dotenv
load_dotenv()


import pdfplumber

def extract_text_from_pdf(pdf_path):
    all_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            all_text += page.extract_text() + "\n"
    return all_text

if __name__ == "__main__":
    pdf_file = "sample.pdf"  # Put a sample PDF file in your folder
    text = extract_text_from_pdf(pdf_file)
    print("Extracted Text:")
    print(text)
