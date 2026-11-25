'''“Shape defines the interface: every shape has area(). Each subclass overrides
 it with its own formula, so code can call shape.area() on any shape without knowing 
 which kind it is. That’s polymorphism. The base class 
raises NotImplementedError so a subclass that forgets to override area() fails loudly.”'''
import math
class Shape():
    def area(self):
        raise NotImplementedError("Name a shape")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        result = self.width * self.height
        return result

class Circle(Shape):
    def __init__(self, radius):
            self.radius = radius
    def area(self):
        result = math.pi * (self.radius**2)
        return result

import math

c = Circle(2)
r = Rectangle(3, 4)

assert isinstance(c, Shape)
assert isinstance(r, Shape)
assert r.area() == 12
assert math.isclose(c.area(), math.pi * 4)

shapes = [Circle(1), Rectangle(2, 5), Circle(3)]
total = sum(shape.area() for shape in shapes)
assert math.isclose(total, math.pi + 10 + math.pi * 9)

try:
    Shape().area()
    assert False, "Expected NotImplementedError"
except NotImplementedError:
    pass

print("All tests passed!")