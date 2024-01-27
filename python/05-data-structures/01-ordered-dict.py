from collections import OrderedDict

# From python3.7 onwards, normal `dict` also preserves insertion order
# Earlier, it did the same too, but only as a side-effect of the 
# cpython implementation, earlier it was not present in the spec.
od = OrderedDict(a = 1, b = 2)
print(od.items())
od["c"] = 3
print(od.items())