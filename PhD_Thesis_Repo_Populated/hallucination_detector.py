def detect_hallucination(response_text):
    hallucination_keywords = ['unverified', 'fictional', 'made up']
    score = sum(1 for word in hallucination_keywords if word in response_text.lower())
    return score / len(hallucination_keywords)
