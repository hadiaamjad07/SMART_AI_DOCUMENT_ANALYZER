# ==========================================================
# AI SMART DOCUMENT ANALYZER
# Developed by Hadia Awan
# ==========================================================

import streamlit as st

from pdf_reader import extract_pdf_text
from docx_reader import extract_docx_text
from txt_reader import extract_txt_text

from prompt import (
    summary_prompt,
    keyword_prompt
)

from analyzer import (
    check_ollama,
    get_models,
    generate_response,
    ask_document
)

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="AI Smart Document Analyzer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

.stApp{
    background-color:#0E1117;
    color:white;
}

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

[data-testid="stSidebar"]{
    background:#161B22;
}

.stButton>button{

    width:100%;
    background:#2563EB;
    color:white;
    border-radius:10px;
    border:none;
    font-weight:bold;
    padding:10px;
}

.stButton>button:hover{

    background:#1D4ED8;
    color:white;

}

[data-testid="stFileUploader"]{

    border:2px dashed #2563EB;
    border-radius:12px;
    padding:15px;

}

.block-container{

    padding-top:2rem;

}

.metric-box{

    background:#1F2937;
    padding:15px;
    border-radius:10px;

}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.title("📄 AI Analyzer")

    st.markdown("---")

    # -----------------------------------
    # OLLAMA STATUS
    # -----------------------------------

    if check_ollama():

        st.success("🟢 Ollama Online")

    else:

        st.error("🔴 Ollama Offline")
        st.info("Run : ollama serve")

    st.markdown("---")

    # -----------------------------------
    # MODEL SELECTION
    # -----------------------------------

    st.subheader("🤖 AI Model")

    models = get_models()

    selected_model = st.selectbox(

        "Choose Model",
        models

    )

    st.markdown("---")

    st.subheader("📂 Supported Files")

    st.write("✅ PDF")
    st.write("✅ DOCX")
    st.write("✅ TXT")

    st.markdown("---")

    st.subheader("🚀 Features")

    st.write("📄 AI Summary")
    st.write("📌 Key Points")
    st.write("🔑 Keywords")
    st.write("💬 Ask AI")
    st.write("📥 Download Report")

# ==========================================================
# MAIN PAGE
# ==========================================================

st.title("📄 AI Smart Document Analyzer")

st.subheader(
    "Analyze any PDF, DOCX or TXT file using Artificial Intelligence"
)

st.write(
    "Upload your document and let AI understand, summarize, and answer questions."
)

st.divider()

# ==========================================================
# FILE UPLOADER
# ==========================================================

uploaded_file = st.file_uploader(

    "Choose a document",

    type=[
        "pdf",
        "docx",
        "txt"
    ]

)
# ==========================================================
# FILE DETAILS
# ==========================================================

if uploaded_file is not None:

    st.success("✅ Document Uploaded Successfully!")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "📄 File Name",
            uploaded_file.name
        )

    with col2:
        st.metric(
            "📦 File Size",
            f"{round(uploaded_file.size / 1024, 2)} KB"
        )

    with col3:
        extension = uploaded_file.name.split(".")[-1].upper()

        st.metric(
            "📁 File Type",
            extension
        )

    st.divider()

    # ======================================================
    # EXTRACT TEXT
    # ======================================================

    text = ""

    if extension == "PDF":

        text = extract_pdf_text(uploaded_file)

        st.subheader("📄 Extracted PDF Text")

    elif extension == "DOCX":

        text = extract_docx_text(uploaded_file)

        st.subheader("📝 Extracted DOCX Text")

    elif extension == "TXT":

        text = extract_txt_text(uploaded_file)

        st.subheader("📄 Extracted TXT Text")

    else:

        st.error("Unsupported File Format")

    # ======================================================
    # DOCUMENT STATISTICS
    # ======================================================

    characters = len(text)

    words = len(text.split())

    lines = len(text.splitlines())

    reading_time = max(1, words // 200)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "🔤 Characters",
            f"{characters:,}"
        )

    with c2:
        st.metric(
            "📝 Words",
            f"{words:,}"
        )

    with c3:
        st.metric(
            "📄 Lines",
            f"{lines:,}"
        )

    with c4:
        st.metric(
            "📖 Reading Time",
            f"{reading_time} min"
        )

    st.divider()

    # ======================================================
    # DOCUMENT PREVIEW
    # ======================================================

    with st.expander(
        "📄 View Extracted Document",
        expanded=False
    ):

        st.text_area(
            "Document Content",
            value=text,
            height=350
        )

else:

    st.info("⬆️ Upload a PDF, DOCX, or TXT document to begin analysis.")
    # ==========================================================
# AI DOCUMENT ANALYSIS
# ==========================================================

if uploaded_file is not None:

    st.divider()

    st.subheader("🤖 AI Smart Analysis")

    if st.button("🚀 Analyze with AI"):

        with st.spinner("🤖 AI is analyzing your document..."):

            prompt = summary_prompt(text)

            summary = generate_response(
                prompt,
                selected_model
            )

        st.success("✅ AI Analysis Completed Successfully!")

        st.markdown(summary)

        st.download_button(
            label="📥 Download AI Report",
            data=summary,
            file_name="AI_Document_Report.txt",
            mime="text/plain",
            key="download_report"
        )

    # ======================================================
    # AI KEYWORDS
    # ======================================================

    st.divider()

    st.subheader("🔑 AI Keywords")

    if st.button("Generate Keywords"):

        with st.spinner("Extracting keywords..."):

            keyword_result = generate_response(
                keyword_prompt(text),
                selected_model
            )

        keywords = keyword_result.split("\n")

        for keyword in keywords:

            keyword = keyword.strip()

            if keyword:

                st.markdown(
                    f"""
<div style="
background:#1F2937;
padding:12px;
margin-bottom:8px;
border-left:5px solid #2563EB;
border-radius:8px;">
🔹 <b>{keyword}</b>
</div>
""",
                    unsafe_allow_html=True
                )

    # ======================================================
    # ASK AI
    # ======================================================

    st.divider()

    st.subheader("💬 Ask AI About Your Document")

    question = st.text_input(
        "Ask anything about this document..."
    )

    if st.button("🤖 Ask AI"):

        if question.strip() == "":

            st.warning("⚠ Please enter a question.")

        else:

            with st.spinner("Thinking..."):

                answer = ask_document(
                    text,
                    question,
                    selected_model
                )

            st.success("✅ Answer")

            st.write(answer)

# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.caption(
    "Developed with ❤️ using Python, Streamlit and Ollama"
)