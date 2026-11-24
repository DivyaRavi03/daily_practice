import functools

def announce(func):
    @functools.wraps(func)                 # keeps greet's real name
    def wrapper(*args, **kwargs):          # accepts any arguments
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)     # run the original
        print(f"Finished {func.__name__}")
        return result                      # hand back its answer unchanged
    return wrapper

@announce
def greet(name):
    return f"Hello, {name}!"

result = greet("Divya")
# Calling greet
# Finished greet
assert result == "Hello, Divya!"