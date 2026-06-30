# ==========================================================
# AI SMART DOCUMENT ANALYZER
# pdf_reader.py
# ==========================================================

import PyPDF2


def extract_pdf_text(uploaded_file):
    """
    Extract text from PDF.
    """

    text = ""

    try:

        pdf_reader = PyPDF2.PdfReader(uploaded_file)

        for page in pdf_reader.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text + "\n"

    except Exception as e:

        text = f"Error reading PDF: {e}"

    return text


def get_pdf_info(uploaded_file):
    """
    Return PDF information.
    """

    try:

        pdf_reader = PyPDF2.PdfReader(uploaded_file)

        return {
            "pages": len(pdf_reader.pages),
            "encrypted": pdf_reader.is_encrypted
        }

    except Exception:

        return {
            "pages": 0,
            "encrypted": False
        }