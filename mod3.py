"""
MODULE 3: Keyword Gap Analysis & Result Display
-------------------------------------------------------------
Responsibilities:
- Compare job description keywords vs resume keywords
- Identify important keywords missing from the resume
- Package the final result (score + missing keywords) for display
"""

# Common words to ignore even after stopword removal (too generic to matter)
IGNORE_WORDS = {
    "and", "the", "for", "with", "you", "your", "our", "are", "will",
    "have", "has", "this", "that", "from", "who", "job", "work", "role"
}


def get_missing_keywords(clean_resume_text, clean_jd_text, top_n=15):
    """
    Finds keywords present in the job description but missing from the resume.
    Returns: list of missing keywords (max top_n)
    """
    resume_words = set(clean_resume_text.split())
    jd_words = set(clean_jd_text.split())

    missing = jd_words - resume_words
    # keep only meaningful words: length > 3 and not in ignore list
    missing = [w for w in missing if len(w) > 3 and w not in IGNORE_WORDS]

    return sorted(missing)[:top_n]


def build_result(match_score, missing_keywords):
    """
    Packages the final result for display in the app.
    Returns: dictionary with score, verdict, and missing keywords
    """
    if match_score >= 75:
        verdict = "Strong Match"
    elif match_score >= 50:
        verdict = "Moderate Match"
    else:
        verdict = "Weak Match"

    return {
        "match_score": match_score,
        "verdict": verdict,
        "missing_keywords": missing_keywords,
    }


# Quick standalone test (run this file directly to test Module 3 alone)
if __name__ == "__main__":
    resume_text = "python developer flask sql experience django"
    jd_text = "looking for python developer experience flask sql rest apis docker aws"

    missing = get_missing_keywords(resume_text, jd_text)
    result = build_result(72.5, missing)

    print(result)