# GP
#  a*r^0 a*r^1  a*r^2
# a = 2
# r = 2
# n = 4
# for i in range(n):
#     # 0 1 2 3
#  *   print(a * r**i)

# ....................................................
# patterns

"""
*****
*   *
*   *
*   *
*****

****
*...*
*...*
*...*
*****
"""
# n = 9
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
"""

    *
   ***
  *****
 *******
*********

....*
...***
..*****
.*******
*********
"""
# n
# i=1  =>4 (n-1) (n-i)  1     5     2*i-1 => 1
# i=2 => 3 (n-2)        3     4     2*i-1=>  3
# i=3 => 2              5     3           => 5
# i=4 => 1              7     2           => 7
# i=5 => 0              9     1           => 9


n = 7
# for i in range(n, 0, -1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(2 * i - 1):
#         print("*", end="")
#     print()
# for i in range(n, 0, -1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(2 * i - 1):
#         if k == 0 or k == 2 * i - 2 or i == n:
#             print("*", end="")
#         else:
#             print(" ", end="")

#     print()

# Data types
#  Primitive  => immutable
# Non Primitive  => mutable

# LIST
# x = ["chips", "candies"]
# a = [1, 2, 3, 4]
# print(a, len(a))
# a[1] = 5
# print(type(a), len(a))

# for i in a:
#     print(i + 3)

# K = []
# print(K)
# K = [1, 2, 3, "Sam", "Danny", True, 3.4, [1, 4, 5, 6, 7]]

# # Replacing
# # K[4] = "Hi"

# # print(K)

# #  Add Replace Remove/Delete  Slicing indexing

# #  K[start: end : step]

# X = K[-1:-3:-1]

# print(X)
# print(K)
