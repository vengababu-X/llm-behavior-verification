def sample_responses(call_fn, prompt: str, k: int = 10):
    return [call_fn(prompt) for _ in range(k)]
