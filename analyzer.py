# ==========================================================
# AI SMART DOCUMENT ANALYZER
# analyzer.py
# ==========================================================

import requests

# ==========================================================
# OLLAMA CONFIGURATION
# ==========================================================

OLLAMA_URL = "http://localhost:11434"

# ==========================================================
# CHECK OLLAMA STATUS
# ==========================================================

def check_ollama():
    """
    Check whether Ollama server is running.
    """

    try:

        response = requests.get(
            f"{OLLAMA_URL}/api/tags",
            timeout=3
        )

        return response.status_code == 200

    except Exception:

        return False


# ==========================================================
# GET INSTALLED MODELS
# ==========================================================

def get_models():
    """
    Return all installed Ollama models.
    """

    try:

        response = requests.get(
            f"{OLLAMA_URL}/api/tags"
        )

        models = response.json()["models"]

        return [
            model["name"]
            for model in models
        ]

    except Exception:

        return ["llama3.2:1b"]


# ==========================================================
# GENERATE AI RESPONSE
# ==========================================================

def generate_response(prompt, model):
    """
    Generate response using Ollama.
    """

    payload = {

        "model": model,
        "prompt": prompt,
        "stream": False

    }

    response = requests.post(

        f"{OLLAMA_URL}/api/generate",

        json=payload

    )

    if response.status_code == 200:

        return response.json()["response"]

    return "Error generating response."


# ==========================================================
# ASK QUESTIONS ABOUT DOCUMENT
# ==========================================================

def ask_document(document, question, model):
    """
    Ask AI questions about uploaded document.
    """

    prompt = f"""
You are an AI Smart Document Analyzer.

Rules:

- Answer ONLY using the uploaded document.
- Never make up information.
- If the answer is not available, reply:

"I couldn't find that information in the document."

Document:

{document}

Question:

{question}

Answer:
"""

    return generate_response(
        prompt,
        model
    )


# ==========================================================
# DOCUMENT SUMMARY
# ==========================================================

def document_summary(document, model):
    """
    Generate document summary.
    """

    prompt = f"""
Summarize the following document.

Include:

1. Summary
2. Important Points
3. Main Topic
4. Difficulty Level
5. Final Conclusion

Document:

{document}
"""

    return generate_response(
        prompt,
        model
    )


# ==========================================================
# EXTRACT KEYWORDS
# ==========================================================

def extract_keywords(document, model):
    """
    Extract keywords from document.
    """

    prompt = f"""
Extract the 10 most important keywords.

Rules:

- One keyword per line
- No numbering
- No explanation

Document:

{document}
"""

    return generate_response(
        prompt,
        model
    )


# ==========================================================
# DOCUMENT STATISTICS
# ==========================================================

def document_statistics(text):
    """
    Calculate document statistics.
    """

    words = len(text.split())

    characters = len(text)

    lines = len(text.splitlines())

    reading_time = max(1, words // 200)

    return {

        "words": words,

        "characters": characters,

        "lines": lines,

        "reading_time": reading_time

    }