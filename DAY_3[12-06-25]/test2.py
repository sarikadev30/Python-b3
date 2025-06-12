# LOGICAL OPERATORS

# AND Operator => True if All Values are True

# print(True and False)
# print(False and False)
# print(False and True)
# print(True and True )
# print(True and True and False)

# a = True
# b = False
# print(a and b)

# p = 3 > 5
# q = 9 >= 8
# print(p and q)
# print(p or q)

# x = p and q
# z = p or q
# print(not z)  # False
# print(not x)  # True

# OR Operator => If Any one Value is True it will return True

# print(True or False)
# print(True or True or False)  #
# print(False or True or False)  #
# print(False or True)
# print(False or False)

# NOT Operator => It will change to opposite value

# print(not True)
# print(not False)

# .................................................................
# Problem :
# a = 9 < 11
# b = 2 == 3
# c = 10 > 3
# result = a and (b or c)
# print(result)
# .................................................................

# x = 4 <= 4
# y = 10 < 5
# z = not (x and y)
# print(z)


# .................................................................

# m = 0 != 0
# n = 1 == 1
# o = m and not n
# print(o)


# .................................................................

# p = 6 == 6
# q = 5 != 5
# r = not (p or q)
# print(r)

# .................................................................

# p = 10 < 5
# q = 3 == 3
# r = 7 != 7
# result = not (p or q and r)
# print(result)
# .............................................................

# Assignment Operators
# x = 27
# x = x + 2  # =>  x+=2
# x -= 2
# x *= 2
# x /= 2
# x %= 2
# x //= 2  # Floor Division
# print(x)
# .......................................................
# x = 8
# x *= 2
# x -= 4
# print(x)  # 12
# ........................................................
# a = 5
# b = 3
# a %= b
# print(a)  # 2
# .......................................................
# x = 101
# x -= 25
# x //= 5
# print(x)
# # .......................................................
# b = 10
# b %= 4
# b *= 2
# print(b)
# .......................................................

# Swap the values without using the third variable
# a = 1
# b = 2

# a = a + b    # 3
# b = a - b    # 2
# a = a - b    # 1

# a, b = b, a
# print(a, b)
# ..............................................................
# Membership Operators

# text = "hello world"
# print("h" in text)
# print("z" not in text)
# ...............................................................
# greeting = "good morning"
# print("good" in greeting)
# print("Good" in greeting)
# print("night" not in greeting)
# .............................................................
# a = [12, 23, 34, 24]
# b = [12, 23, 34, 24]
# print(a is b)

x = "hello"
y = "hello"
print(x is not y)

# a = 300
# b = 300
# print(a is b)
# ............................................................
# x = 3
# print("Start")
# if x == 2:
#     print("Ya the number is 2")
# print("End")
# # .............................................................
# # Print "Its Hot" if the temperature is above 40
# a = 34
# print("Start")
# if a > 40:
#     print("Its Hot!.......")
# else:
#     print("Not Hot.......")
# print("End")


# ..............................................................
# Print "UPPERCASE LETTER" if the character is uppercase
# a = input("Enter a character: ")
# if a.isupper():
#     print("UPPERCASE LETTER")
# else:
#     print("Not a uppercase")
# ............................................................
# Print "Even Number" if the input number is even or odd
# x = 56
# print("Start")
# if x % 2 == 0:
#     print("Even number")
# else:
#     print("Odd Number")
# print("End")
# ................................................................
# Print "In Range" if the number is in between 20 and 30
# <20  Below
# >30  Above
# 20 or 30  Equal
# ................................................
# # to check number is positive, negative or zero

# if-elif-else
x = 0
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")
