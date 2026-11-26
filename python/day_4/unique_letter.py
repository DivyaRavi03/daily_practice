def first_unique(text):
    items = {}
    for letter in text:
        items[letter] = 1 + items.get(letter, 0)
    for key in items:
        if items[key] == 1:
            return key
    return None