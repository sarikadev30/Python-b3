"""
1  2  3  4  5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
"""

# n = 5
# matrix = [[0] * n for i in range(n)]
# # boundaries
# left = 0
# right = n - 1
# top = 0
# bottom = n - 1
# num = 1

# while top <= bottom or left <= right:
#     # left to right
#     for i in range(left, right + 1):
#         matrix[top][i] = num
#         num += 1
#     top += 1

#     # top to bottom
#     for i in range(top, bottom + 1):
#         matrix[i][right] = num
#         num += 1
#     right -= 1

#     # right to left
#     for i in range(right, left - 1, -1):
#         matrix[bottom][i] = num
#         num += 1
#     bottom -= 1

#     # bottom to top
#     for i in range(bottom, top - 1, -1):
#         matrix[i][left] = num
#         num += 1
#     left += 1

# print(matrix)

# for i in range(n):
#     for j in range(n):
#         # print(matrix[i][j], end=" ")
#         print(f"{matrix[i][j]:2}", end=" ")
#     print()


# x = [1, 2, 3, 4, 5, 6, 7, 9, 4, 2]
# x[3] = 45

# y = "sam"
# # y[1] = "b"
# print(y[1])

# z = "34"
# z = int(z)
# print(type(z))
# .......................................................................
# Set
"""
x = [1, 2, 3, 4, 5, 6, 7, 9, 4, 2, 1, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4]
# Creation of Set
y = {3, 5, 1, 2, 3}
print(y, x[2:5])
print(type(y))

# Searching in Sets

print(5 in y)
print(90 in y)

# Functions in Sets

# List to Set
a = set(x)
print("a", a)

# Set to List
b = list(y)
print(b)

# Adding A Element to the Set
a.add(34)
print("a", a)

#  Another Way to create set
r = set((1, 2, 3, 4, "Sam", 54.89))
print(r)

# Access the Elements
t = {"apple", "banana", "cherry"}
for x in t:
    print(x)

#  Removing An element => remove() and discard()
# r.remove(4)
# r.discard(4)
# remove() => It will raise error if value is not present
# discard() => It will not raise error if value is not present

# r.remove(72)
# r.discard(72)
# print(r)

# Adding List to the set
setA = {2, 3, 4, 5, 6}
listA = [1, 6, 7, 9, 0, 5, 6]
print(setA)

setA.update(listA)
print(setA)

# Clear the Set or make the set Empty => clear()
setA.clear()
print(setA)
"""
# .......................................................................
# even_numbers = {2, 4, 6, 8, 10}
# prime_numbers = {2, 3, 5, 7}
# intersection = even_numbers & prime_numbers
# print(intersection)
# # even_numbers = even_numbers - intersection
# even_numbers -= intersection
# print(even_numbers)


# ....................................................................
# letters = set("mississippi")
# print(letters, len(letters))
# # letters.pop()
# print(letters.pop(), letters)
# # letters.pop()
# # print(letters)

# # 1-21 to the list
# za = list(range(1, 22))
# zb = set(range(1, 22))
# print(za, zb)
# .....................................................................
# Tuple
#  Create => Indexing => Slicing => Merging
t = (1, 2, 3, "Sam", 67, 34, 2, 3)
t1 = ("apple", "banana", "mango")
print(t, type(t))
# t.append(45)
# t[3] = 89
# t.pop()
print(t[3], t[3:6], type(t))
# Merging
t2 = t + t1
print(t2)

K = (1, 6, 7, 40, 0, 4, 66, 46, 33, 89, "Danny", (1, 4, 3, 5), [1, 4, 6])
# print(K[-1:-4:-1])

# Looping
for i in range(len(K)):  # 0 1 2 3 .....len(K)
    print(K[i])

for j in K:
    print(j)


#  Conversion of Tuple and List
# convert tuple to list
# add the element
# again convert it to tuple

# K = list(K)
# print(K)
# K.append(34.89)
# print(K)
# K = tuple(K)
# print(K, len(K))
