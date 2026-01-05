import time

def sample_responses(call_fn, prompt: str, k: int = 2, delay: float = 3.0):
    responses = []
    for _ in range(k):
        responses.append(call_fn(prompt))
        time.sleep(delay)
    return responses
