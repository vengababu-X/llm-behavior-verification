def structure_metrics(response: str):
    sentences = response.count(".")
    length = len(response)

    return {
        "length": length,
        "sentences": sentences,
        "avg_sentence_length": length / max(1, sentences)
    }


def validate_structure(metrics: dict, min_length: int):
    assert metrics["length"] >= min_length, "Response too short"
