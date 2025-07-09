# Special Functions
# Special functions are built-in functions or anonymous functions
# that enhance Python’s expressiveness and functional programming capabilities

# print(len("Python"))

# LAMBDA Funnction => anonymous function (no name)  (map , filter )


# def fun(x):
#     s = x * x
#     print(s)


# fun(5)

# s = lambda x: x * x
# print(s(5))
# ................................................................................
# Map => map(function,iterable)
# a = [1, 2, 3, 4, 5, 6, 7]

# x = list(map(lambda z: z % 2 == 0, a))
# print(x, a)

# Filter => filter(function, iterable) => Takes onlt True Values
# a = [1, 2, 3, 4, 5, 6, 7]
# x = list(filter(lambda z: z % 2 == 0, a))
# print(x, a)

# ..........................................................................
# Sorted => Sorts the list  sorted(listName, key, reverse)
a = [3, 4, 2, 6, 9, 10]
b = ["Sam", "Fam", "Hello", "Danny"]
c = [["Sam", 34], ["Danny", 23], ["Fam", 45], ["Leo", 12]]


# x=sorted(a)
# x = sorted(b, reverse=True)
# print(x)

# z = sorted(c, reverse=True)
# z = sorted(c,key=lambda a: a[0])
# print(z)


d = {"a": 3, "b": 1, "c": 2}
pairs = [(1, 3), (2, 2), (4, 1)]
words = ["apple", "banana", "apricot", "cherry", "avocado"]
# z = sorted(d.items(), key=lambda x: x[1])
# z = sorted(pairs, key=lambda x: x[0])
# print(z)
# ..........................................................................
# Sum
# ..........................................................................
# zip  => combine the iterables
# words = ["apple", "banana", "apricot", "cherry", "avocado"]
# b = ["Sam", "Fam", "Hello", "Danny", "Leo"]
# z = list(zip(b, words, b))
# print(z)

# ..........................................................................
# isinstance  => type checking

# z = isinstance(10, int)
# z = isinstance("Sam", int)
# print(z)

# .........................................................................
# dir => get all the methoda and variables of particular directory
# x = dir("Python")
# print(x)
# ........................................................................
#  reduce  => cumulatively

# reduce(function,iterable)
# from functools import reduce

# a = [1, 2, 3]


# print(reduce(lambda x, y: x * y, a))
# ..........................................................................
# import sys

# print(sys.path)
