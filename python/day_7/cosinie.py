import math
def cosine_similarity(a,b):
    total = 0
    if len(a) != len(b):
        raise ValueError("Can't compute with different lengths of lists")
    else:
        len_a = 0
        len_b = 0
        for x, y in zip(a,b):
            product = x * y
            total += product
            len_a = x * x
            total += len_a
            len_b = y * y
            total += len_b
        sqrt_a = math.sqrt(len_a)
        sqrt_b = math.sqrt(len_b)
        if sqrt_a == 0 or sqrt_b ==0:
            raise ValueError("Cant divide with 0")
        cosine = total / (sqrt_a * sqrt_b)
    return cosine
            
import math

assert math.isclose(cosine_similarity([1, 0], [1, 0]), 1.0)      # same direction
assert math.isclose(cosine_similarity([1, 0], [0, 1]), 0.0)      # at right angles
assert math.isclose(cosine_similarity([1, 2], [-1, -2]), -1.0)   # opposite
assert math.isclose(cosine_similarity([1, 2, 3], [2, 4, 6]), 1.0)  # same direction, different length
assert math.isclose(cosine_similarity([1, 2], [3, 4]), 11 / (math.sqrt(5) * 5))

for a, b in [([1, 2], [1, 2, 3]), ([0, 0], [1, 2])]:
    try:
        cosine_similarity(a, b)
        assert False, "Expected ValueError"
    except ValueError:
        pass

print("All tests passed!")