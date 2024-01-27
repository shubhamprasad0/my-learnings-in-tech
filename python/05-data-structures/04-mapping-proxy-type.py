from types import MappingProxyType

writable = {
    "one": 1,
    "two": 2,
    "three": 3,
}

read_only = MappingProxyType(writable)

print(read_only["one"])

try:
    read_only["two"] = 4
except TypeError as e:
    print(f"Could not write to read_only: {e}")