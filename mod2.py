"""
MODULE 2: AI Matching Engine (Score Generation)
-------------------------------------------------------------
Responsibilities:
- Convert resume text and job description text into TF-IDF vectors
- Compute cosine similarity between them
- Return a match score as a percentage
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_match_score(clean_resume_text, clean_jd_text):
    """
    Computes similarity between resume and job description.
    Returns: match score (float, 0-100)
    """
    documents = [clean_resume_text, clean_jd_text]

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    match_score = round(similarity * 100, 2)
    return match_score


# Quick standalone test (run this file directly to test Module 2 alone)
if __name__ == "__main__":
    resume_text = "python developer flask sql rest api experience django"
    jd_text = "looking for python developer experience flask sql rest apis"

    score = get_match_score(resume_text, jd_text)
    print(f"Match Score: {score}%")