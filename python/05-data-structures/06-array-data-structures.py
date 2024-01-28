from array import array

# ---------------------- list -----------------------
l1 = ["hello", 1, 2, 3]
print(l1) # ["hello", 1, 2, 3]
l1.append("world")
print(l1) # ["hello", 1, 2, 3, "world"]
l1.pop()
print(l1) # ["hello", 1, 2, 3]
l1.insert(0, "world")
print(l1) # ["world", "hello", 1, 2, 3]
l1.extend([4, 5, 6])
print(l1) # ["world", "hello", 1, 2, 3, 4, 5, 6]

# ---------------------- tuple -----------------------
t1 = ("hello", 1, 2, 3)
print(t1)

# can't modify t1, as tuple is immutable
try:
    t1[0] = 2
except TypeError as e:
    print(e)


# -------------------- array.array -------------------
a1 = array('i', [1, 2, 3, 4])
print(a1)
print(len(a1))

a2 = array('f')
print(len(a2))
a2.append(2.5)
print(len(a2))
print(a2)

try:
    # this fails because arrays accept a specific type which is defined earlier (here, float)
    a2.append("hello")
except TypeError as e:
    print(e)

