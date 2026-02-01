# Main Streamlit App
import streamlit as st
import os

from ingestion.pdf_reader import extract_text_from_pdf
from ingestion.docx_reader import extract_text_from_docx
from ingestion.text_cleaner import clean_text
from language.language_detector import detect_language
from nlp.clause_segmenter import segment_clauses
from nlp.ner_extractor import extract_entities
from nlp.obligation_classifier import classify_obligation
from nlp.ambiguity_detector import detect_ambiguity
from risk_engine.pattern_detector import detect_patterns
from risk_engine.risk_scorer import score_clause
from llm.explainer import explain_clause

st.title("Contract Analysis & Risk Assessment Bot")

file = st.file_uploader("Upload Contract", ["pdf", "docx", "txt"])

if file:
    os.makedirs("storage/uploads", exist_ok=True)
    path = f"storage/uploads/{file.name}"
    with open(path, "wb") as f:
        f.write(file.read())

    if file.name.endswith(".pdf"):
        text = extract_text_from_pdf(path)
    elif file.name.endswith(".docx"):
        text = extract_text_from_docx(path)
    else:
        text = open(path, encoding="utf-8").read()

    text = clean_text(text)
    lang = detect_language(text)
    clauses = segment_clauses(text)

    st.write("Detected Language:", lang)
    st.write("Total Clauses:", len(clauses))

    for c in clauses:
        ent = extract_entities(c["text"])
        obl = classify_obligation(c["text"])
        amb = detect_ambiguity(c["text"])
        pat = detect_patterns(c["text"])
        risk = score_clause(pat, obl, amb["score"])

        with st.expander(f"{c['clause_id']} — {risk['level']}"):
            st.write(c["text"])
            st.write("Entities:", ent)
            st.write("Risk Reasons:", risk["reasons"])
            st.write("Explanation:", explain_clause(c["text"], risk["level"], risk["reasons"]))
