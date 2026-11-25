'''return vs yield: return gives one value and ends the function. yield gives 
one value and pauses, remembering where it stopped, so it can continue later. 
That’s why a generator 
can hand out a huge file’s lines one at a time without holding them all in memory.'''

# def read_lines(filename):
#     with open(filename, 'r') as file:
#         for line in file:
#             yield line.rstrip('\n')

# import types

# with open("big.txt", "w") as f:
#     for i in range(1, 100001):
#         f.write(f"line {i}\n")

# gen = read_lines("big.txt")
# assert isinstance(gen, types.GeneratorType)
# assert next(gen) == "line 1"
# assert next(gen) == "line 2"

# count = sum(1 for _ in read_lines("big.txt"))
# assert count == 100000

# with open("empty.txt", "w") as f:
#     f.write("")
# assert list(read_lines("empty.txt")) == []

# print("All tests passed!")

def count_to_three():
    print("start")
    yield 1
    print("after 1")
    yield 2
    print("after 2")
    yield 3

g = count_to_three()
print("created")
print(next(g))
print(next(g))