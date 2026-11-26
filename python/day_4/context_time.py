import time

class Timer():
    def __init__(self, value):
        self.value = value

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        end = time.perf_counter()
        self.elapsed = end - self.start
        print(f"{self.value} took {self.elapsed:.4f} seconds")
        return False

import time

with Timer("sleep test") as t:
    time.sleep(0.2)
assert 0.2 <= t.elapsed < 0.5

# try:
#     with Timer("error test") as t2:
#         time.sleep(0.1)
#         raise ValueError("boom")
#     assert False, "Expected ValueError"
# except ValueError:
#     pass
# assert t2.elapsed >= 0.1

print("All tests passed!") 
# A context manager guarantees setup and cleanup around a block. 
# __enter__ runs at the start, __exit__ runs at the end even if the block raises, 
# and returning False from __exit__ lets the error propagate. 
# File handling with with open(...) works the same way.”

# Every fix here was one of five you’d already seen: 
# self. for saved data (Stack), return self (t is the object), 
# () to call a function (decorator warm-up), and the True/False rule from your own answer.
#  So try the next one with one more hint before asking for code.   