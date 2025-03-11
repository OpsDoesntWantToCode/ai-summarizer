from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
import streamlit as st
import re

MIN_INPUT_LENGTH = 30

def summarize_text(text, model, tokenizer, min=30, max=100):  
    if not text.strip():
        return "⚠️ Error: No text provided for summarization."
    
    if len(text.split()) < MIN_INPUT_LENGTH:
        return f"⚠️ Please enter at least {MIN_INPUT_LENGTH} words for better summarization."

    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(**inputs, max_length=max, min_length=min, length_penalty=1.0, 
                                 do_sample=False, eos_token_id=model.config.eos_token_id, num_beams=4,
                                 no_repeat_ngram_size=2)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    if st.session_state.get("use_bullet_points", False):
        # Ensure the last sentence is complete
        sentences = re.split(r"(?<=\.) ", summary)  # Split at periods followed by a space
        
        # If the last sentence is too short (possibly incomplete), remove it
        if len(sentences) > 1 and len(sentences[-1].split()) < 5:  
            sentences.pop()

        # Format as bullet points
        summary = "\n- " + "\n- ".join(sentences)
    return summary

def check_summarize_button(button, summary): 
    if button:
        st.subheader("Summary:")
        st.write(summary)
