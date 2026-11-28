import time
class TTLCache:
    def __init__(self, ttl):
        self.ttl = ttl
        self.store = {}
        if self.ttl <= 0:
            raise ValueError("TTL cannot be less than 0")

    def set(self, key, value):
        self.store[key] = [value,time.monotonic()] # again simply overwrites it with a fresh time, which restarts its timer.

    def get(self, key):
        if key not in self.store:
            return None
        if (time.monotonic()-self.store[key][1]) <= self.ttl:
            return self.store[key][0]
        self.store.pop(key)
        return None

    def size(self):
        return len(self.store)


import time

cache = TTLCache(0.5)
cache.set("a", 1)
cache.set("b", 2)
assert cache.get("a") == 1
assert cache.get("missing") is None
assert cache.size() == 2

time.sleep(0.6)
assert cache.get("a") is None       # expired
assert cache.size() == 1            # "a" was removed by get; "b" not checked yet

cache.set("c", 3)
time.sleep(0.3)
cache.set("c", 30)                  # replacing restarts the timer
time.sleep(0.3)
assert cache.get("c") == 30         # 0.3s since last set, still fresh

try:
    TTLCache(0)
    assert False, "Expected ValueError"
except ValueError:
    pass

print("All tests passed!")