def valid_paranthe(string):
    brackets = {
        "(":")",
        "[":"]",
        "{":"}"
    }
    stack = []
    for index, item in enumerate(string):
        if item in brackets:
            stack.append(item)
        if item in brackets.values():
            if len(stack) == 0:
                return False
            open = stack.pop(-1)
            if brackets[open] != item:
                return False
    if len(stack) ==0:
        return True
    return False

# print(valid_paranthe("([{}])"))
tests = ["()", "()[]{}", "{[]}", "(]", "([)]", "()(", ")"]
for t in tests:
    print(t, valid_paranthe(t))