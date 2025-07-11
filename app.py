# app.py – DocuMind AI: Smart Document Comparator

import streamlit as st
import docx2txt
import fitz  # PyMuPDF
import difflib
import ollama

# --- Helper: Extract text from supported formats ---
def extract_text(file):
    if file.name.endswith(".pdf"):
        with fitz.open(stream=file.read(), filetype="pdf") as doc:
            return "\n".join(page.get_text() for page in doc)
    elif file.name.endswith(".docx"):
        return docx2txt.process(file)
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    return ""

# --- Compare text ---
def compare_texts(text1, text2):
    diff = difflib.ndiff(text1.splitlines(), text2.splitlines())
    changes = [line for line in diff if line.startswith("+ ") or line.startswith("- ")]
    return "\n".join(changes)

# --- Summarize via LLM ---
def summarize_doc(text, label="Document"):
    prompt = f"""
You are an AI assistant. Summarize the key points of this {label} in simple terms:

{text[:3000]}
"""
    return query_llm(prompt)

# --- Explain comparison ---
def explain_diff(diff_text):
    prompt = f"""
You are a legal/compliance assistant. Here's a diff between two documents. Explain what was added, removed, or changed in simple terms:

{diff_text[:3000]}
"""
    return query_llm(prompt)

# --- LLM wrapper ---
def query_llm(prompt):
    response = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# --- Streamlit UI ---
st.set_page_config(page_title="DocuMind AI", layout="wide")
st.title("🧾 DocuMind AI – Smart Document Comparator")

st.markdown("Upload two documents to compare and summarize their contents.")
col1, col2 = st.columns(2)

with col1:
    file1 = st.file_uploader("Upload Document 1", type=["pdf", "docx", "txt"], key="file1")
with col2:
    file2 = st.file_uploader("Upload Document 2", type=["pdf", "docx", "txt"], key="file2")

if file1 and file2:
    with st.spinner("Reading and analyzing documents..."):
        text1 = extract_text(file1)
        text2 = extract_text(file2)
        diff_result = compare_texts(text1, text2)
        summary1 = summarize_doc(text1, "Document 1")
        summary2 = summarize_doc(text2, "Document 2")
        explanation = explain_diff(diff_result)

    st.markdown("### 📄 Document Summaries")
    st.subheader("📝 Summary – Document 1")
    st.markdown(summary1)

    st.subheader("📝 Summary – Document 2")
    st.markdown(summary2)

    st.markdown("### 🔍 Differences Between Documents")
    st.code(diff_result, language="diff")

    st.markdown("### 🧠 AI Explanation of Changes")
    st.markdown(explanation)
else:
    st.info("Please upload two documents to start comparing.")
