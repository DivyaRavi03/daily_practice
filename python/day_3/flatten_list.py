def flatten(list_items):
    output = []
    for item in list_items:
        if isinstance(item, list):
            another = flatten(item)
            output.extend(another)
        else:
            output.append(item)
    return output

print(flatten([1, [2, 3], 4]))
assert flatten([1, 2, 3]) == [1, 2, 3]
assert flatten([1, [2, 3], 4]) == [1, 2, 3, 4]
assert flatten([1, [2, [3, [4, [5]]]]]) == [1, 2, 3, 4, 5]
assert flatten([[1, 2], [], [3, [4]]]) == [1, 2, 3, 4]
assert flatten(["a", ["b", ["c"]]]) == ["a", "b", "c"]
assert flatten([]) == []

print("All tests passed!")