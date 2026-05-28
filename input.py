from typing import List


def chunk_text(text: str, max_chars: int = 2000) -> List[str]:
    chunks: List[str] = []
    current = ""

    for line in text.split("\n"):
        # If adding this line would exceed the limit → start new chunk
        if len(current) + len(line) + 1 > max_chars:
            if current:
                chunks.append(current.strip())
            current = line
        else:
            if current:
                current += "\n" + line
            else:
                current = line

    if current:
        chunks.append(current.strip())

    return chunks


def clean_text(text: str) -> str:
    return " ".join(text.split())
