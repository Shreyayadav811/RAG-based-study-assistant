"""
    Load a PDF and extract text from each page.

    Returns a list of dictionaries containing:
    - text: extracted text from the page
    - source: path of the PDF
    - page: page number
    """

from pypdf import PdfReader


def load_pdf(path: str):
    

    reader = PdfReader(path)

    documents = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""

        documents.append({
            "text": text,
            "source": path,
            "page": i + 1
        })

    return documents