from sklearn.metrics.pairwise import cosine_similarity

def semantic_similarity(prompt_embedding, response_embeddings):
    return [
        cosine_similarity([prompt_embedding], [emb])[0][0]
        for emb in response_embeddings
    ]


def validate_semantic(similarities, threshold):
    avg_sim = sum(similarities) / len(similarities)
    assert avg_sim >= threshold, f"Low semantic similarity: {avg_sim}"
