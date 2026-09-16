"""
MODULE 1: Resume & Job Description Input + Text Extraction
-------------------------------------------------------------
Responsibilities:
- Extract raw text from an uploaded resume (PDF)
- Clean/pre-process both resume text and job description text
  (lowercase, remove special characters, remove extra whitespace)
"""

import re
import pdfplumber


def extract_text_from_pdf(pdf_file):
    """
    Extracts raw text from a PDF file.
    pdf_file: a file path (string) OR a file-like object (e.g. from Streamlit uploader)
    Returns: extracted text as a single string
    """
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


def clean_text(raw_text):
    """
    Cleans text: lowercase, removes special characters/extra spaces.
    Returns: cleaned text as a single string
    """
    text = raw_text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)   # remove special characters
    text = re.sub(r"\s+", " ", text).strip()    # remove extra whitespace
    return text


def process_inputs(resume_pdf_file, jd_raw_text):
    """
    Main entry point for Module 1.
    Takes the uploaded resume file + raw job description text.
    Returns: (clean_resume_text, clean_jd_text)
    """
    raw_resume_text = extract_text_from_pdf(resume_pdf_file)
    clean_resume_text = clean_text(raw_resume_text)
    clean_jd_text = clean_text(jd_raw_text)
    return clean_resume_text, clean_jd_text


# Quick standalone test (run this file directly to test Module 1 alone)
if __name__ == "__main__":
    sample_resume_path = "resume.pdf"   # place a sample resume.pdf in this folder
    sample_jd = "We are looking for a Python developer with experience in Flask, SQL, and REST APIs."

    resume_clean, jd_clean = process_inputs(sample_resume_path, sample_jd)
    print("----- CLEAN RESUME TEXT -----")
    print(resume_clean[:500])
    print("\n----- CLEAN JD TEXT -----")
    print(jd_clean)