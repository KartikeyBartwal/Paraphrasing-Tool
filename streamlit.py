import streamlit as st
import time
import random
import io
import docx2txt

def paraphrase(text):
    # This is a dummy paraphrasing function
    words = text.split()
    paraphrased_words = [random.choice([w.upper(), w.lower(), w.capitalize()]) for w in words]
    return ' '.join(paraphrased_words)

def read_docx(file):
    return docx2txt.process(file)

st.set_page_config(page_title="Beautiful Paraphrasing Tool", page_icon="📝", layout="wide")

st.title("🛠️ Paraphrasing Tool 🛠️")

st.markdown("""
<style>
    .stTextInput > div > div > input {
        font-size: 18px;
    }
    .stTextArea > div > div > textarea {
        font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)

input_method = st.radio("Choose input method:", ("Text Input", "Document Upload"))

if input_method == "Text Input":
    input_text = st.text_area("Enter your text to paraphrase:", height=200)
else:
    uploaded_file = st.file_uploader("Choose a document", type=["txt", "docx"])
    if uploaded_file is not None:
        if uploaded_file.type == "text/plain":
            input_text = str(uploaded_file.read(), "utf-8")
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            input_text = read_docx(uploaded_file)
        st.write("Document content:")
        st.write(input_text)
    else:
        input_text = ""

if st.button("Paraphrase", key="paraphrase_button"):
    if input_text:
        with st.spinner("Paraphrasing in progress..."):
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.1)  # Simulate processing for 10 seconds
                progress_bar.progress(i + 1)
            
            paraphrased_text = paraphrase(input_text)
            st.success("Paraphrasing complete!")
        
        st.subheader("Paraphrased Text:")
        st.write(paraphrased_text)
    else:
        st.warning("Please enter some text or upload a document to paraphrase.")