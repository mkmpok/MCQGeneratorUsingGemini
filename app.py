import streamlit as st
from gemini_wrapper import get_response
import PyPDF2

st.title("Automated MCQ Generator with Gemini")
st.write("Upload a PDF and/or enter your own text to generate MCQs.")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
pdf_text = ""

if uploaded_file is not None:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    for page in pdf_reader.pages:
        content = page.extract_text()
        if content:
            pdf_text += content
    st.success("PDF uploaded and text extracted.")

# Text Input
manual_text = st.text_area("You can also type or paste additional text here:")

# Combine both PDF + manual text
combined_text = pdf_text + "\n" + manual_text

if st.button("Generate MCQs"):
    if combined_text.strip() == "":
        st.warning("⚠️ Please upload a PDF and/or enter some text.")
    else:
        with st.spinner("Generating questions..."):
            prompt = f"Generate 4 multiple-choice questions with answers based on the following text:\n\n{combined_text}"
            mcqs = get_response(prompt)
            st.success("MCQs Generated!")
            st.write(mcqs)
