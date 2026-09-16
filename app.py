"""
MAIN APPLICATION
-------------------------------------------------------------
Connects Module 1 (Extraction), Module 2 (Matching Engine),
and Module 3 (Keyword Analysis) into one Streamlit web app.
"""

import streamlit as st
from module1_extraction import process_inputs
from module2_matching import get_match_score
from module3_keywords import get_missing_keywords, build_result

st.set_page_config(page_title="AI Resume Screener", page_icon="\U0001F4C4")
st.title("\U0001F4C4 AI Resume Screener")
st.write("Upload a resume and paste a job description to see how well they match.")

# ---- Inputs ----
resume_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
jd_text = st.text_area("Paste Job Description", height=200)

if st.button("Analyze Resume"):
    if resume_file is None or not jd_text.strip():
        st.warning("Please upload a resume and enter a job description.")
    else:
        # ----- Module 1: Extraction & Pre-processing -----
        clean_resume, clean_jd = process_inputs(resume_file, jd_text)

        # ----- Module 2: AI Matching Engine -----
        score = get_match_score(clean_resume, clean_jd)

        # ----- Module 3: Keyword Analysis & Result -----
        missing_keywords = get_missing_keywords(clean_resume, clean_jd)
        result = build_result(score, missing_keywords)

        # ----- Display Results -----
        st.subheader(f"Match Score: {result['match_score']}%")
        st.progress(min(int(result["match_score"]), 100))
        st.write(f"**Verdict:** {result['verdict']}")

        st.subheader("Missing Keywords / Skills")
        if result["missing_keywords"]:
            st.write(", ".join(result["missing_keywords"]))
        else:
            st.write("No major missing keywords found. Good match!")