def estimate_tokens(text: str) -> int:
    # rough heuristic: 1 token ≈ 4 chars
    return len(text) // 4