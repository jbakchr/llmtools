import requests
from typing import Optional

OLLAMA_URL = "http://localhost:11434/api/generate"


class LLMError(Exception):
    pass


def generate(prompt: str, model: str = "gpt-oss:120b-cloud", timeout: int = 60) -> str:
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": model,
                "prompt": prompt,
                "stream": False,
            },
            timeout=timeout,
        )
    except requests.RequestException as e:
        raise LLMError(f"Request failed: {e}")

    if response.status_code != 200:
        raise LLMError(f"Ollama error: {response.text}")

    data = response.json()

    if "response" not in data:
        raise LLMError(f"Unexpected response format: {data}")

    return data["response"].strip()