class DefaultAlias:
    def __init__(self, name):
        self.name = name

    def __get__(self, inst, cls):
        if inst is None:
            return self
        return getattr(inst, self.name)


class Alias(DefaultAlias):
    def __set__(self, inst, value):
        print(f"inst: {inst}, value: {value}")
        setattr(inst, self.name, value)

    def __delete__(self, inst):
        delattr(inst, self.name)


class Book:
    def __init__(self, title, short_title=None):
        self.title = title
        if short_title is not None:
            self.short_title = short_title

    short_title = DefaultAlias("title")


b = Book("The Life and Opinions of Tristam Shandy, Gent.")
print(b.short_title)
b.short_title = "Tristam Shandy"
print(b.short_title)
del b.short_title
print(b.short_title)

print("HOLA!))")


class Book:
    def __init__(self, title, short_title=None):
        self.title = title
        if short_title is not None:
            self.short_title = short_title

    short_title = Alias("title")


b = Book("The Life and Opinions of Tristam Shandy, Gent.")
print(b.short_title)
b.short_title = "Tristam Shandy"
print(b.short_title)
del b.short_title
# print(b.short_title)

print("REAL PYTHON")


class Verbose_attribute:
    def __get__(self, obj, type=None) -> object:
        print("accessing the attribute to get the value")
        return 42

    def __set__(self, obj, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")


class Foo:
    attribute1 = Verbose_attribute()


my_foo_object = Foo()
x = my_foo_object.attribute1
print(x)
# my_foo_object.attribute1 = 43
