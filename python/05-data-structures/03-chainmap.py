from collections import ChainMap

d1 = {
    "one": 1,
    "two": 2,
}

d2 = {
    "three": 3,
    "four": 4,
}

cm = ChainMap(d1, d2)

print(cm["one"])
print(cm["three"])


# insertions, deletions, updates only happen on the first dict of the chainmap
cm["five"] = 5
print(d1)

del cm["two"]
print(d1)

cm["three"] = 33
print(d1)
print(d2)
print(cm["three"])