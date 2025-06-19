# Sum of Digits
# 2345 => 2+3+4+5 => 14

# 2345 => sum+=5 => sum+=4
# 2345 => 5

# n = 2345
# a = n
# sum = 0
# while a > 0:
#     r = a % 10
#     sum += r
#     a = a // 10
#     # print(r, sum, a)

# print(sum)
# ............................................................
# For Loop

#  for in sequence:
#   code

# range(start,end,step) => default step=1 default start=0

# for i in range(1, 5, 1):
#     print(i)
# for i in range(1, 5):
#     print(i)
# for i in range(5):
#     print(i)
# for i in range(1, 8, 6):
#     print(i)
# for i in range(10, 0, -1):
#     print(i)
# for i in range(5, -1, -1):
#     print(i)

# for b in range(5):
#     print("Hello")

# Sum of 1 to 10

# 1+2+3+4+5+6+7+8+9+10 => 55
# .................................................
# Print digits in single line
# 01234
# for i in range(5):
#     print(i, end="")

# ...........................................
# Factorial of a number (4!)=> 4*3*2*1 =>24

# x = input("Enter a number: ")
# x = int(x)
# fact = 1
# for i in range(x, 0, -1):
#     fact *= i
# print(fact)


# ......................................................................
# For loop with Break

# for guest in range(1, 11):
#     print("Guest", guest)
#     if guest == 4:
#         break

# .......................................................................
# For Loop with Continue

# for guest in range(1, 11):
#     print("Guest", guest)
#     if guest == 3:
#         continue


# ......................................................................
# for guest in range(1, 11):
#     if guest == 3:
#         continue
#     print("Guest", guest)


# .......................................................................

# count = 1
# for k in range(1, 10):  # 1,2,3,4,5,6,7,8,9
#     count += 1
#     if k == 5:
#         continue

# print(count)

# .....................................................................
# AP Series
# 2,4,6,8 => 20
# 2 a+0*d
# 4 a+1*d
# 6 a+2*d
# 8 a+3*d

# a = int(input("Enter a: "))
# d = int(input("Enter d: "))
# n = int(input("Enter n: "))
# sum = 0
# for i in range(n):
#     # print(a + i * d, i, a, n, d)
#     sum += a + i * d
# print(sum)
# .....................................................................
# Square Series of even number
#
# n = int(input("Enter a number(n) : "))
# x = 0
# for i in range(2, n + 1, 2):
#     x += i**2
# print(x)
# ...................................................................
#  Nested Loop

# for family in range(1, 6):
#     for candy in range(1, 5):
#         print(family, " ate ", candy, " candy")

# 20 times
# ..............................................................
# for i in range(2):
#     for j in range(3):
#         print("Hello")

# i j
# i=0 j=0 0<3 Hello
# i=0 j=1 1<3 Hello
# i=0 j=2 2<3 Hello
# i=0 j=3 3<3 F
# i=1 j=0 0<3 Hello
# i=1 j=1 1<3 Hello
# i=1 j=2 2<3 Hello
# i=1 j=3 3<3 F
# i=2 2<2 F
# ..............................................................
# i = 0
# while i < 2:
#     j = 0
#     while j < 3:
#         print(i, j)
#         print("Hello")
#         j += 1
#     i += 1

# .............................................................
# Father gave the son a target, of completing 10 sets. Each set contains 10 Rounds of a field.
# ............................................................
"""
**********
**********
**********
**********
**********

*
* *
* * *
* * * *
* * * * *


* * * * *
* * * *
* * *
* *
*
"""

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
