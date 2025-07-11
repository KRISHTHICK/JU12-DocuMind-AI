# JU12-DocuMind-AI
GEN AI

🧾 DocuMind AI – Smart Document Comparator & Summary Generator
📄 What It Does
DocuMind AI lets users upload two or more documents (PDF, DOCX, TXT) and:

Compares them side by side

Summarizes their content

Highlights key similarities & differences

Explains in simple terms what changed or is missing

Supports contracts, SOPs, policies, and legal docs

🔍 Core Features
Feature	Description
📁 Multi-file upload	Upload 2–3 PDF, DOCX, or TXT files
🧠 AI Document Summarizer	Generates plain-language summary per doc
🔄 AI Comparator	Compares documents and highlights differences
🧠 Layman Explainer	Explains changes in simple terms
📄 Markdown output	Full output in side-by-side view
📥 Optional: Export as PDF	

🧑‍💻 Tech Stack
Component	Technology
Frontend	Streamlit
Backend AI	Ollama (LLaMA3) or GPT-4
File Parsing	PyMuPDF, python-docx
Text Diff	difflib
Export	pdfkit or fpdf (optional)

🧠 Example Use Case
Compare:

SOP v1 (Feb 2024) and SOP v2 (June 2024)

See added sections, removed clauses, simplified rules

Get summary: "Section 3.1 was removed", "Clause about remote work added"

# 🧾 DocuMind AI – Smart Document Comparator & Summary Generator

DocuMind AI allows you to compare documents side by side, generate summaries, and get AI-powered explanations of the changes between them.

---

## 🔍 Features

- Upload 2 documents (PDF, DOCX, TXT)
- View summarized version of each document
- See word-level differences using text diff
- Get natural language explanation of the changes
- Works great for contracts, SOPs, policies, legal docs

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/yourusername/documind-ai.git
cd documind-ai
pip install -r requirements.txt
ollama pull llama3
streamlit run app.py
