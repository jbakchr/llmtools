from typing import List

from llmtools.client import generate
from llmtools.prompt import render
from llmtools.output import extract_bullets
from llmtools.input import chunk_text


def summarize(
    text: str,
    max_words: int = 100,
    model: str = "gpt-oss:120b-cloud",
) -> str:
    prompt = render(
        """
Summarize the following text.

Rules:
- Maximum {max_words} words
- Be concise and factual
- Do not add information not present in the text

Text:
{text}
""",
        text=text,
        max_words=max_words,
    )

    return generate(prompt, model=model)


def summarize_for_scanning(
    text: str,
    max_bullets: int = 5,
    model: str = "gpt-oss:120b-cloud",
) -> str:
    prompt = render(
        """
Summarize the following text for fast scanning.

Rules:
- Output ONLY bullet points
- Maximum {max_bullets} bullets
- Each bullet: max 12 words
- Focus on key facts, insights, or decisions
- No fluff, no filler language
- Be direct and concrete

Text:
{text}
""",
        text=text,
        max_bullets=max_bullets,
    )

    return generate(prompt, model=model)


def summarize_for_scanning_list(
    text: str,
    max_bullets: int = 5,
    model: str = "gpt-oss:120b-cloud",
) -> list[str]:
    raw = summarize_for_scanning(text, max_bullets=max_bullets, model=model)
    return extract_bullets(raw)


def summarize_chunks(
    text: str,
    model: str = "gpt-oss:120b-cloud",
    max_chars: int = 2000,
) -> str:
    chunks = chunk_text(text, max_chars=max_chars)

    summaries: List[str] = []

    for chunk in chunks:
        summary = generate(f"Summarize this:\n{chunk}", model=model)
        summaries.append(summary)

    combined = "\n".join(summaries)

    
    final = generate(
    f"""
Summarize this into 5 bullet points:
- max 12 words per bullet
- focus on key insights

{combined}
"""
)


    return final
