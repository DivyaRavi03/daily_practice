def read_file(filename):
    try: 
        with open(filename, 'r') as file:
            data = file.read()
            return data
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None

with open("hello.txt", "w") as f:
    f.write("Hello, Divya!")

assert read_file("hello.txt") == "Hello, Divya!"
assert read_file("missing.txt") is None   # should also print the error message

print("All tests passed!")
        