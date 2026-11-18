class Stack:
    def __init__(self):
        self.plates = []
        
    def push(self, item):
        self.plates.append(item)

    def size(self):
        return len(self.plates)
        
    def is_empty(self):
        if self.size() == 0:
            return True
        return False

    def pop(self):
        if self.size() == 0: 
            raise IndexError("There is no item to pop")
        value = self.plates[-1]
        self.plates.pop()
        return value
    
    def peek(self):
        if self.size() == 0: 
                    raise IndexError("There is no item to peek")
        value = self.plates[-1]
        return value
    
    
s = Stack()
assert s.is_empty() == True
assert s.size() == 0

s.push(1)
s.push(2)
s.push(3)
assert s.size() == 3
assert s.peek() == 3
assert s.size() == 3
assert s.pop() == 3
assert s.pop() == 2
assert s.size() == 1
assert s.is_empty() == False
assert s.pop() == 1
assert s.is_empty() == True

for method in (s.pop, s.peek):
    try:
        method()
        assert False, "Expected IndexError"
    except IndexError:
        pass

print("All tests passed!")