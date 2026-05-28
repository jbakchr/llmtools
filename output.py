import json
from typing import List, Dict, Any
from client import generate


def parse_json(text: str) -> Dict[str, Any]:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # Fallback: try to extract JSON block
        start = text.find("{")
        end = text.rfind("}") + 1

        if start != -1 and end != 0:
            try:
                return json.loads(text[start:end])
            except json.JSONDecodeError:
                pass

    raise ValueError("Failed to parse JSON from LLM response")


def generate_json(prompt: str, model: str = "gpt-oss:120b-cloud") -> Dict[str, Any]:
    response = generate(prompt, model=model)
    return parse_json(response)


def extract_bullets(text: str) -> List[str]:
    lines = text.splitlines()

    return [
        line.strip("-• ").strip()
        for line in lines
        if line.strip().startswith(("-", "•"))
    ]