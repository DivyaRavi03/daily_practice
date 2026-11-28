def chunk_text(text, size, overlap):
    if size <= 0 or overlap < 0 or overlap >= size:
        raise ValueError("Need size > 0 and 0 <= overlap < size")

    words = text.split()
    chunks = []
    step = size - overlap                      # how far each chunk's start moves

    for i in range(0, len(words), step):
        chunk = " ".join(words[i:i + size])
        chunks.append(chunk)                   # save it before checking the end
        if i + size >= len(words):             # this chunk reached the last word
            break

    return chunks      

text = "one two three four five six seven eight nine ten"

assert chunk_text(text, 4, 1) == [
    "one two three four",
    "four five six seven",
    "seven eight nine ten",
]
assert chunk_text(text, 4, 0) == [
    "one two three four",
    "five six seven eight",
    "nine ten",
]
assert chunk_text(text, 5, 2) == [
    "one two three four five",
    "four five six seven eight",
    "seven eight nine ten",
]
assert chunk_text("a b c", 10, 2) == ["a b c"]
assert chunk_text("", 3, 1) == []

for size, overlap in [(0, 0), (3, 3), (3, -1)]:
    try:
        chunk_text(text, size, overlap)
        assert False, "Expected ValueError"
    except ValueError:
        pass

print("All tests passed!")