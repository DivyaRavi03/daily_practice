def shout(text):
    return text.upper()

yell = shout                 # no parentheses
print(yell("hi"))

def apply(func, value):
    return func(value)

print(apply(shout, "hey"))

def make_greeter():
    def greeter(name):
        return "Hello, " + name
    return greeter           # no parentheses

g = make_greeter()
print(g("Divya"))