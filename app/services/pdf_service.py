from pypdf import PdfReader


def extract_text(file_path):
    """
    Extract all text from a PDF file.
    """

    reader = PdfReader(file_path)

    document_text = ""

    for page in reader.pages:
        document_text += page.extract_text() or ""

    return document_text