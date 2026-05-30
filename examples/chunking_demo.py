from llmtools import summarize_chunks

long_text = "This is the first chunk of text. It contains some information about a topic. This is the second chunk of text. It contains additional information about the same topic. This is the third chunk of text. It contains even more information about the topic. This is the fourth chunk of text. It contains a summary of the information from the previous chunks. This is the fifth chunk of text. It contains some conclusions about the topic based on the information from the previous chunks."

print("Original text:")
print(long_text)
print(len(long_text), "characters")

print("\nSummarized text:")
result = summarize_chunks(long_text)
print(result)
print(len(result), "characters")

