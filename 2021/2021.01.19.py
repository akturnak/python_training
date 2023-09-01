class M(type):
    def __new__(cls, name, bases, classdict):
        print(f"cls: {cls}")
        print(f"name: {name}")
        print(f"bases: {bases}")
        print(f"classdict: {classdict}")
        for attr in classdict.get("__slots__", ()):
            if attr.startswith("_"):

                def getter(self, attr=attr):
                    return getattr(self, attr)

                classdict["get" + attr[1:]] = getter
        return type.__new__(cls, name, bases, classdict)


class Point(list, metaclass=M):
    __slots__ = ["_x", "_y"]


print(dir(Point))
p = Point()
p._x, p._y = 3, 2
print(p.getx())
print(p.gety())