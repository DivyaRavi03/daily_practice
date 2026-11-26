def rotate(items, number):
    output = []
    if len(items) == 0:
        return []
    else:
        k = number % len(items)
        move_front = items[-k:]
        rest = items[:-k]
        output = move_front + rest
    return output
# I reduce k with k % n, which handles k bigger than the list and negative k. 
# Then the last k items go to the front: items[-k:] + items[:-k]. 
# It’s O(n), and I check for an empty list first to avoid dividing by zero.”

assert rotate([1, 2, 3, 4, 5], 1) == [5, 1, 2, 3, 4]
assert rotate([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
assert rotate([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]
assert rotate([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]
assert rotate([1, 2, 3, 4, 5], 7) == [4, 5, 1, 2, 3]
assert rotate([1, 2, 3, 4, 5], -1) == [2, 3, 4, 5, 1]
assert rotate([], 3) == []

nums = [1, 2, 3]
rotate(nums, 1)
assert nums == [1, 2, 3]

print("All tests passed!")