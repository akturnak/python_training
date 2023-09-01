class CachedAttribute:
    def __init__(self, method, name=None):
        print(f" method: {method}, name: {name}")
        self.method = method
        self.name = name or method.__name__

    def __get__(self, inst, cls):
        print(f"self: {self}, inst: {inst}, cls: {cls}")
        if inst is None:
            return self
        result = self.method(inst)
        setattr(inst, self.name, result)
        return result


class CachedClassAttribute(CachedAttribute):
    def __get__(self, inst, cls):
        print(f"class.__get__: self: {self}, inst: {inst}, cls: {cls}")
        return super().__get__(cls, cls)


class MyObject:
    def __init__(self, n):
        self.n = n

    @CachedAttribute
    def square(self):
        return self.n * self.n


m = MyObject(23)
print(vars(m))
print(m.square)
print(vars(m))
del m.square
print(vars(m))
m.n = 42
print(m.square)
print(vars(m))


class MyClass:
    class_attr = 23

    @CachedClassAttribute
    def square(cls):
        print("square!")
        return cls.class_attr * cls.class_attr


x = MyClass()
y = MyClass()
print(x.square)
print(y.square)

# del MyClass.square
print(x.square)