import os
import requests

API_URL = os.getenv("LLM_API_URL")
API_KEY = os.getenv("LLM_API_KEY")

def call_llm(prompt: str, temperature=0.2) -> str:
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(API_URL, json=payload, headers=headers, timeout=30)
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]
