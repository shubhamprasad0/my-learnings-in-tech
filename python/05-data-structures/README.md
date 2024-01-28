# Data Structures in Python

## Dicts

1. `dict`
2. `collections.OrderedDict` -- Preserves insertion order of keys
3. `collections.defaultdict` -- Returns a default value if key is missing
4. `collections.ChainMap` -- Treats a collection of dicts as a single dict
5. `types.MappingProxyType` -- Used to create a read-only version of a dict
6. `collections.Counter` -- Used to keep counts of keys; similar to a frequency mapping

## Array data structures

1. `list` -- can hold arbitrary types of objects, can grow and shrink in size, dynamic arrays
2. `tuple` -- same as list, but immutable
3. `array.array` -- similar to C arrays, contiguous typed data
4. `str` -- contiguous, immutable array of unicode characters
5. `bytes` -- immutable array of bytes (0 to 255), cannot hold anything else
6. `bytearray` -- similar to bytes, but mutable