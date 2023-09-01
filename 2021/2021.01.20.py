import copy


def freshdefaults(f):
    fdefaults = f.__defaults__

    def refresher(*args, **kwargs):
        f.__defaults__ = copy.deepcopy(fdefaults)
        return f(*args, **kwargs)

    return refresher


@freshdefaults
def packitem(item, pkg=[]):
    pkg.append(item)
    return pkg


item = "one"
pack = packitem(item)
print(pack)
pack = packitem(item)
print(pack)
pack = packitem(item)
print(pack)
pack = packitem(item, pack)
print(pack)

"""
    ['one']
    ['one']
    ['one']
    ['one', 'one']
"""

print("standard behavior")


def packitem2(item, pkg=[]):
    pkg.append(item)
    return pkg


item = "one"
pack = packitem2(item)
print(pack)
pack = packitem2(item)
print(pack)
pack = packitem2(item)
print(pack)
pack = packitem2(item, pack)
print(pack)

"""
    ['one']
    ['one', 'one']
    ['one', 'one', 'one']
    ['one', 'one', 'one', 'one']
"""
