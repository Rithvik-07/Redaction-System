import streamlit as st
import fitz  # PyMuPDF
import docx
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

st.title(" Document Redaction & Anonymization System")
def extract_pdf(file):
    text = ""
    pdf = fitz.open(stream=file.read(), filetype="pdf")
    for page in pdf:
        text += page.get_text()
    return text
def extract_docx(file):
    doc = docx.Document(file)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text
option = st.radio("Choose input type:", ["Text", "PDF", "DOCX"])

text = ""

if option == "Text":
    text = st.text_area("Enter text")

elif option == "PDF":
    file = st.file_uploader("Upload PDF", type=["pdf"])
    if file:
        text = extract_pdf(file)
        st.success("PDF text extracted successfully")

elif option == "DOCX":
    file = st.file_uploader("Upload DOCX", type=["docx"])
    if file:
        text = extract_docx(file)
        st.success("DOCX text extracted successfully")
mode = st.selectbox(
    "Choose anonymization type",
    ["redact", "replace", "highlight"]
)
if st.button("Process") and text:

    analyzer = AnalyzerEngine()
    anonymizer = AnonymizerEngine()

    results = analyzer.analyze(text=text, language="en")

    if mode == "redact":
        output = anonymizer.anonymize(text=text, analyzer_results=results).text

    elif mode == "replace":
        output = anonymizer.anonymize(text=text, analyzer_results=results).text

    else:
        output = text  # placeholder for highlight mode

    st.subheader("📄 Output")
    st.write(output)

    st.download_button(
        "Download Output",
        output,
        file_name="redacted_output.txt"
    )
