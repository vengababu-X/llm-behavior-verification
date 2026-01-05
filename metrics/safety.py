def validate_safety(responses, banned_terms):
    for response in responses:
        text = response.lower()
        for term in banned_terms:
            assert term not in text, f"Banned term detected: {term}"
