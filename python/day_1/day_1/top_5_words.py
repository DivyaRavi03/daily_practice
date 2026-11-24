def top_words(file):
    word_dict={}
    with open(file) as f:
        for line in f:
            words = line.split()
            for word in words:
                word = word.lower()
                word = word.strip(",.:;/?!")
                word_dict[word]=1+word_dict.get(word, 0)
    sorted_dict = sorted(word_dict.items(), key=lambda s:s[-1], reverse=True)
    return sorted_dict[:5]

with open("sample.txt", "w") as f:
    f.write("Apple banana apple cherry. Banana apple, date!\n")
    f.write("Cherry apple banana apple? Elderberry date banana.\n")
    f.write("Apple cherry, cherry fig; banana date elderberry.\n")

with open("short.txt", "w") as f:
    f.write("Hi hi there")

with open("empty.txt", "w") as f:
    f.write("")

assert top_words("sample.txt") == [
    ("apple", 6), ("banana", 5), ("cherry", 4), ("date", 3), ("elderberry", 2)
]
assert top_words("short.txt") == [("hi", 2), ("there", 1)]
assert top_words("empty.txt") == []

print("All tests passed!")