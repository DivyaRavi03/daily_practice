def group_anagrams(items):
    output = []
    hashset = {}
    for item in items:
        key = "".join(sorted(item.lower()))
        hashset[key]=hashset.get(key,[]) + [item]
    return list(hashset.values())

print(group_anagrams(["listen", "silent", "enlist", "google", "gogole", "cat"]) == [
    ["listen", "silent", "enlist"],
    ["google", "gogole"],
    ["cat"],
])

# assert group_anagrams(["listen", "silent", "enlist", "google", "gogole", "cat"]) == [
#     ["listen", "silent", "enlist"],
#     ["google", "gogole"],
#     ["cat"],
# ]
# assert group_anagrams(["Tea", "eat", "ate", "tan", "nat"]) == [
#     ["Tea", "eat", "ate"],
#     ["tan", "nat"],
# ]
# assert group_anagrams(["a"]) == [["a"]]
# assert group_anagrams([]) == []

# print("All tests passed!")
