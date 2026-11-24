import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter() - start_time
        print (f"{func.__name__} took {end_time:.4f} seconds")
        return result
    return wrapper

import time

@timer
def slow_add(a, b):
    time.sleep(0.2)
    return a + b

@timer
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

assert slow_add(2, 3) == 5
assert greet("Divya") == "Hello, Divya!"
assert greet("Divya", greeting="Hi") == "Hi, Divya!"
assert slow_add.__name__ == "slow_add"

print("All tests passed!")