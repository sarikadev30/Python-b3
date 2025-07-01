# Fibonacci Series
# 0 1 1 2 3 5 8
# def fun(n):
#     a, b = 0, 1
#     result = []
#     for i in range(n):
#         result.append(a)
#         a, b = b, a + b
#     return result


# res = fun(8)
# print(res[-1])
# print(fun(8)[-1])
# .......................................................................

# Scope
# 4 => Local Scope , Enclosing Scope , Global Scope , built-In Scope

"""
def fun():
    x = 90                # Local Scope
    print(x)


# print(x)

fun()
"""
"""
x = 34  # Global Scope


def fun():
    msg = "Hi"
    global x
    x = 78
    print(x)


fun()
print(x)
"""


#  Enclosing Scope
"""
def fun():
    x = 78
    print(x)

    def innerFun():
        nonlocal x
        x = 56
        print(x)

    innerFun()
    print(x)


fun()
"""
"""
x = 23
def fun():
    x = 78
    print("3", x)

    def innerFun():
        global x
        x = 56
        print("4", x)

    innerFun()
    print("5", x)


print("1", x)
fun()
print("2", x)
"""

# Built-In Scope

# a = "Sam"
# print(len(a))
# int()
# max()

# print(__builtins__)


# .............................................................
# x = 10
# def my_func():
#     x = 20
#     print(x)


# my_func()
# print(x)


# ................................................................
# x = 100


# def change():
#     global x
#     print(x)
#     x = 200
#     print(x)


# change()
# print(x)


# ..................................................................
# x = 5


# def outer():
#     x = 10

#     def inner():
#         print(x)

#     inner()


# outer()
# print(x)


# .................................................................
# def outer():
#     x = "local"

#     def inner():
#         nonlocal x
#         x = "nonlocal"

#     inner()
#     print("x inside outer:", x)


# outer()
# print(x)


# ............................................................
# def func():
#     print(x)

# x = 50
# func()


# ...........................................................

# x = 10

# # print(y)
# y = 78
# print(y)


# def func():
#     # global x
#     print(x)
#     x = 20
#     print(x)


# func()
# ...........................................................
# x = "global"
# def outer():
#     x = "outer"

#     def inner():
#         print("inner:", x)

#     inner()
#     print("outer:", x)

# outer()
# print("global:", x)
# ..........................................................
# PYTHON EXECPTIONS
# print(10 / 0)
# x = int(input("Enter a value: "))
# print("x", x)
# z = [1, 2, 3, 4]
# print(z[5])

# ...............................................................................
# try-except block
# x = int(input("Enter a number: "))
# try:
#     a = 10 / x
#     print(a)
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# ..............................................................................
# multiple-except block
# try:
#     x = int(input("Enter a number: "))
#     a = 10 / x
#     print(a)
# except ValueError:
#     print("Cannot Change String to Integer!...")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")

# print("Continue.......")
# ...................................................................
# Catching multiple exceptions together
# try:
#     x = int(input("Enter a number: "))
#     a = 10 / x
#     print(a)
# except (ValueError, ZeroDivisionError) as e:
#     print("Error!...", e)

# print("Continue.......")

# ...................................................................
# Generic exception handling

# try:
#     x = int(input("Enter a number: "))
#     a = 10 / x
#     print(a)
# except Exception as e:
#     print("Error occurred:", e)

# .................................................................
# Finally Block
# try:
#     x = int(input("Enter a number: "))
#     a = 10 / x
#     print(a)
# except Exception as e:
#     print("Error occurred:", e)
# finally:
#     print("This block always runs.")
#     print("Exception Handles")
# ...............................................................
# Raise an Exception

# x = int(input("Enter a number: "))
# if x == 0:
#     raise ValueError("x cannot be zero")
# try:
#     a = 10 / x
#     print(a)
# except Exception as e:
#     print("Error occurred:", e)
# finally:
#     print("This block always runs.")
#     print("Exception Handles")


# ...............................................................
#  User Defined Exception
