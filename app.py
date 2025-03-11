import streamlit as st
from pdf_utils import extract_text_from_pdf
from summarizer import summarize_text, check_summarize_button
from transformers import MBartForConditionalGeneration, MBart50Tokenizer

# Initialize session state
if "model" not in st.session_state:
    model_name = "facebook/mbart-large-50"
    st.session_state.tokenizer = MBart50Tokenizer.from_pretrained(model_name)
    st.session_state.model = MBartForConditionalGeneration.from_pretrained(model_name)

# Streamlit UI
st.title("📄 AI Summarizer")
st.write("Summarize text manually or upload a document.")

# 📌 Sidebar for Settings
st.sidebar.header("⚙️ Settings")
st.session_state.use_bullet_points = st.sidebar.checkbox("Format output as bullet points", value=False)
st.session_state.min_length = st.sidebar.number_input("Minimum summary length", min_value=30, max_value=1000, value=30, step=1)
st.session_state.max_length = st.sidebar.number_input("Maximum summary length", min_value=30, max_value=1000, value=100, step=1)

if (st.session_state.min_length > st.session_state.max_length):
    st.sidebar.warning("Minimum length should be less than maximum length.")
    st.session_state.min_length = st.session_state.max_length
    
# Create tabs for better organization
tab1, tab2 = st.tabs(["📄 PDF Summarizer", "✍️ Manual Text Summarizer"])

# 📄 PDF Summarization
with tab1:
    st.subheader("Upload a PDF to Summarize")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"], accept_multiple_files=False)

    if uploaded_file is not None:
        text_input = extract_text_from_pdf(uploaded_file)
        summarize_button = st.button("Summarize PDF")

        summary = summarize_text(text_input, st.session_state.model, st.session_state.tokenizer, 
                                 st.session_state.min_length, st.session_state.max_length)
        check_summarize_button(summarize_button, summary)

# ✍️ Manual Text Summarization
with tab2:
    st.subheader("Enter Text to Summarize")
    text_input = st.text_area("Enter text:", height=200)

    summarize_button = st.button("Summarize Text")

    summary = summarize_text(text_input, st.session_state.model, st.session_state.tokenizer, 
                                 st.session_state.min_length, st.session_state.max_length)
    check_summarize_button(summarize_button, summary)