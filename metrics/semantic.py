import math

def text_vector(text: str):
    words = text.lower().split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq

def cosine_sim(v1, v2):
    common = set(v1.keys()) & set(v2.keys())
    num = sum(v1[w] * v2[w] for w in common)

    den1 = math.sqrt(sum(v**2 for v in v1.values()))
    den2 = math.sqrt(sum(v**2 for v in v2.values()))

    if den1 == 0 or den2 == 0:
        return 0.0
    return num / (den1 * den2)

def semantic_similarity(prompt, responses):
    p_vec = text_vector(prompt)
    scores = []
    for r in responses:
        r_vec = text_vector(r)
        scores.append(cosine_sim(p_vec, r_vec))
    return scores
