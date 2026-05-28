from client import generate
from prompt import render
from output import extract_bullets, parse_json, generate_json
from input import chunk_text


# ---------------------------
# 1. Simple prompt rendering + generate
# ---------------------------

def example_simple():
    print("\n--- Example: Simple Generate ---")

    prompt = render(
        "Give me 3 short bullet points about {topic}",
        topic="Python programming",
    )

    response = generate(prompt)

    print("\nRaw response:")
    print(response)

    bullets = extract_bullets(response)

    print("\nParsed bullets:")
    print(bullets)


# ---------------------------
# 2. Chunking + summarization
# ---------------------------

def example_chunking():
    print("\n--- Example: Chunking + Summarization ---")

    long_text = (
        "Python is a high-level programming language.\n"
        "It is widely used for backend systems, scripting, and AI.\n"
        "It has a simple syntax and large ecosystem.\n"
        "Many developers use it for automation and data science.\n"
    ) * 5  # simulate long text

    chunks = chunk_text(long_text, max_chars=150)

    print(f"\nNumber of chunks: {len(chunks)}")

    summaries = []

    for i, chunk in enumerate(chunks):
        print(f"\nSummarizing chunk {i + 1}...")
        result = generate(f"Summarize this:\n{chunk}")
        summaries.append(result)

    combined = "\n".join(summaries)

    final_summary = generate(
        f"Combine and shorten the following summaries:\n{combined}"
    )

    print("\nFinal summary:")
    print(final_summary)


# ---------------------------
# 3. Structured JSON output
# ---------------------------

def example_json():
    print("\n--- Example: JSON Parsing ---")

    prompt = """
Return a JSON object with:
- title
- summary

Text:
Python is a programming language used for many tasks including AI and scripting.
"""

    response = generate(prompt)

    print("\nRaw response:")
    print(response)

    try:
        data = parse_json(response)

        print("\nParsed JSON:")
        print(data)
        print("\nTitle:", data.get("title"))
        print("Summary:", data.get("summary"))

    except Exception as e:
        print("\nFailed to parse JSON:", e)


# ---------------------------
# MAIN
# ---------------------------

if __name__ == "__main__":
    # example_simple()
    # example_chunking()
    # example_json()

    data = generate_json("""
    Return JSON:
    {
    "title": string,
    "summary": string
    }

    Text:
    Python is widely used for AI and backend systems.
    """)

    print(data)
    print(data["title"])
    print(data["summary"])
