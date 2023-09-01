Foo = type("Foo", (), {})
x = Foo()
print(x)


class Foo:
    pass


x = Foo()

print(x)

Bar = type("Bar", (Foo,), dict(attr=100))

x = Bar()
print(x.attr)
print(x.__class__)
print(x.__class__.__bases__)


def f(self):
    print(f"attr={self.attr}")


Foo = type("Foo", (), {"attr": 100, "attr_val": f})
x = Foo()
print(x.attr)
x.attr_val()


def new(cls):
    x = object.__new__(cls)
    x.attr = 100
    return x


Foo.__new__ = new
f = Foo()
print(f.attr)
g = Foo()
print(g.attr)


class Meta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.attr = 100
        return x


class Foo(metaclass=Meta):
    pass


print(f"Foo.attr: {Foo.attr}")


def class_decorator(cls):
    class NewClass(cls):
        attr = 100

    return NewClass


@class_decorator
class X:
    pass


print(f"X.attr: {X.attr}")


import math


class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area():
        doc = "Area of the rectangle"

        def fget(self):
            return self.x * self.y

        def fset(self, value):
            ratio = math.sqrt((1.0 * value) / self.area)
            self.x *= ratio
            self.y *= ratio

        def fdel(self):
            raise AttributeError("It is not allowed!")

        return locals()

    area = property(**area())

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"


rect = Rectangle(3, 5)
print(f"rect: {rect}")
print(f"rect.area: {rect.area}")
rect.area = 10
print(f"rect: {rect}")
print(f"rect.area: {rect.area}")
try:
    del rect.area
except AttributeError as e:
    print(f"error: {e}")
