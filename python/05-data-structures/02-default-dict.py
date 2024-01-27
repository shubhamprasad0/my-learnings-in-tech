from collections import defaultdict

# defaultdict constructor takes a callable
# When a key is missing, the return value of this callable will be used as the default value
dd = defaultdict(list)

dd["dog"].append("tommy")
dd["cat"].append("kitty")
dd["dog"].append("bruno")
dd["cat"].append("meowie")

print(dd["dog"])
print(dd["cat"])

# leveraging the fact that default value of int is 0
# so, int() returns 0
counts = defaultdict(int)

counts['a'] += 1
counts['b'] += 1
counts['b'] += 1

print(counts['a'])
print(counts['b'])