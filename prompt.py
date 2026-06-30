# ==========================================================
# AI SMART DOCUMENT ANALYZER
# prompt.py
# ==========================================================

# ==========================================================
# DOCUMENT SUMMARY PROMPT
# ==========================================================

def summary_prompt(text):

    return f"""
You are an AI Smart Document Analyzer.

Analyze the following document carefully.

Return your answer exactly in this format.

📄 Summary:
Write a short summary of the document.

📌 Important Points:
• Point 1
• Point 2
• Point 3
• Point 4
• Point 5

🎯 Main Topic:
Write one sentence.

📚 Difficulty Level:
Easy / Medium / Hard

😊 Sentiment:
Positive / Neutral / Negative

✅ Final Conclusion:
Write a concise conclusion.

Document:

{text}
"""


# ==========================================================
# KEYWORD EXTRACTION PROMPT
# ==========================================================

def keyword_prompt(text):

    return f"""
You are an AI Document Analyzer.

Extract ONLY the 10 most important keywords.

Rules:

- One keyword per line
- No numbering
- No bullet points
- No explanation
- Maximum 3 words per keyword

Document:

{text}
"""


# ==========================================================
# QUESTION ANSWERING PROMPT
# ==========================================================

def question_prompt(document, question):

    return f"""
You are an AI assistant.

Answer ONLY from the uploaded document.

Rules:

- Do not guess.
- Do not invent information.
- If the answer is not found, reply:

"I couldn't find that information in the document."

Document:

{document}

Question:

{question}

Answer:
"""


# ==========================================================
# DOCUMENT TITLE PROMPT
# ==========================================================

def title_prompt(text):

    return f"""
Read the following document and generate a suitable title.

Rules:

- Maximum 8 words
- Professional
- Clear
- No explanation

Document:

{text}
"""


# ==========================================================
# DOCUMENT CATEGORY PROMPT
# ==========================================================

def category_prompt(text):

    return f"""
Identify the category of this document.

Possible categories:

- Resume
- Report
- Research Paper
- Assignment
- Article
- Letter
- Invoice
- Business Proposal
- Legal Document
- Other

Document:

{text}
"""


# ==========================================================
# DOCUMENT LANGUAGE PROMPT
# ==========================================================

def language_prompt(text):

    return f"""
Identify the language of this document.

Return only the language name.

Document:

{text}
"""