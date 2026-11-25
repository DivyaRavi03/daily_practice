import requests

def fetch_json(url, timeout=2, retries = 3, backoff = 1):
    for attempt in range(retries):
        try:
            results = requests.get(url, timeout=timeout)
            results.raise_for_status()
            return results.json()
        except (requests.Timeout, requests.ConnectionError) as e:
            last_error = e                             # temporary: retry
        except requests.HTTPError as e:
            status = e.response.status_code
            if 400 <= status <= 499:
                raise                                  # our request is wrong: stop now
            last_error = e                             # 5xx, the server's problem: retry

        if attempt < retries - 1:                      # wait only if another attempt is coming
            wait = backoff * 2 ** attempt
            print(f"Attempt {attempt + 1} failed, retrying in {wait}s")
            time.sleep(wait)

    raise last_error 



import time
import requests

# 1. Success
data = fetch_json("https://httpbin.org/json")
assert "slideshow" in data

# 2. 404: raise right away, no retries
start = time.time()
try:
    fetch_json("https://httpbin.org/status/404", backoff=0.5)
    assert False, "Expected HTTPError"
except requests.HTTPError:
    pass
assert time.time() - start < 2

# 3. 500: retry, then raise
start = time.time()
try:
    fetch_json("https://httpbin.org/status/500", retries=3, backoff=0.2)
    assert False, "Expected HTTPError"
except requests.HTTPError:
    pass
assert time.time() - start >= 0.6     # waited 0.2 + 0.4

# 4. Timeout: retry, then raise
try:
    fetch_json("https://httpbin.org/delay/3", retries=2, timeout=1, backoff=0.2)
    assert False, "Expected Timeout"
except requests.Timeout:
    pass

print("All tests passed!")