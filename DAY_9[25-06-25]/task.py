"""
# List
a = [12, 23, 34, 45, 56, 67, 78, 34, 23]
print(a)

# Set
b = set(a)
print(b)

# Tuple
c = tuple(a)
print(c)
"""

# .....................................................................
# Dictionary
# CRUD

# CREATE
# a = {"name": "Sam", "age": 23, "subject": "Maths", 3: "45"}
# print(a)
# print(a["age"])

# b = dict({1: "Sam", 2: "Danny"})
# print(b)

# # READ
# print(a)
# print(a["age"], b[2])
# # Type
# print(type(b))
# # Length
# print(len(b))

# d = {
#     "name": ["Anny", "Bunny", "Danny", "Enav"],
#     "age": [25, 36, 22, 12],
#     "income": [90, 75, 80, 93],
#     "name": "Sam",
# }

# print(d["name"])
# print(d.get("name"))
# print(len(d["name"]))

# print(d["name"][len(d["name"]) - 1])  # Enav
# print(d["name"][len(d["name"]) - 1], " - ", d["age"][len(d["age"]) - 1])

# Loop
# for i in d:
#     # print(i, d[i])
#     print(d[i][len(d[i]) - 1])


# for
# UPDATE
# a = {"name": "Sam", "age": 45, "roll": 23}
# print(a)
# a["age1"] = 12
# print(a)

# DELETE
# pop
# popitem
# clear
# del
# a.pop("roll")
# print(a)

# a.popitem()
# print(a)

# a.clear()
# print(a)

# del a["name"]
# del a
# print(a)

# a = {"name": "Sam", "age": 45, "roll": 23}
# get
# print(a.get("age"))
# print(a.get("age1", "Not Present"))

# keys
# print(a.keys())

# values
# print(a.values())

# items
# print(a.items())
"""
a = "hello hello heelo world wordl world wrold heleo helol"
z = a.split()
print(z)
d = {}
for i in z:
    # print(d.get([i], 0))
    d[i] = d.get(i, 0) + 1
print(d)
"""

# ......................................................
# FUNCTIONS


def channel():
    x = "Sam"
    print("Hello", x)


# channel()
# channel()
# channel()
# channel()
# channel()

# Looping


#
def add(x, y):
    t = x + y
    print(t)


# add(12, 34)
# add(45, 12)
# Default Argument
def subtract(a, b=1):
    print(a - b)


# subtract(6)


# Variable-length Argument
def sumA(*t):
    print(t)
    print(sum(t))


# sumA(1, 2)
# sumA(1, 2, 3)
# sumA(1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 0)


# Keyworded Agrument
def record(name, age):
    print(name, age)


print(record("sam", 45))

# record(age=23, name="Sam")


# Print => values
def fun(z, y):
    total = z + y
    return total


# Diff between Print and return
print(fun(4, 7))
ad = fun(4, 9)
print(ad)
