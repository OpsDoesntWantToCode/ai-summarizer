# AI SUMMARIZER
#### Video Demo:  <https://youtu.be/K6y6E_g_BmI>
#### Description:
A tool that can read pdfs and input text and turn it into key ideas that are easy to digest.
## requirements.txt
- `streamlit`: A framework for building web apps.
- `PyPDF2`: A PDF library, capable of extracting text from pdf files.
- `tiktoken, sentencepiece`: Tokenizing text to feed to the model.
- `transformers`: Providing model for summarize text.
- `torch`: A machine learning framework which is neccesary for model to excute.
## pdf_utils.py
- `extract_text_from_pdf(uploaded_file)`:

Function for extracting text from `uploaded_file`.
If there is no text in the file, `⚠️ No text found in this PDF.` message will be returned.

## settings.py

We will use `json` library for managing settings.

- `load_settings()`:
Loading `settings.json` which stores 3 default settings
  - `"use_bullet_points": False,`: Summary will be formatted in just one single paragraph.
  - `"min_length": 30, "max_length": 100`: The min and max length of the summary.

- `save_settings(new_settings)`: Adjust the json file base on changes of the settings

## summarizer.py


