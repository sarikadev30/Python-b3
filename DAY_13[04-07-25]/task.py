# with open("modules/data.txt", "r+") as f:
#     content = f.read()
#     # print(f.tell())
#     # f.seek(10)
#     # f.write("11th")
#     print(content)

# Path => Absolute Path , Relative Path
# ......................................................................
# Locating Modules
# import sys

# print(sys.path)
# ......................................................................
# Random Module  => In nuile module
# import random

# random.randint(a,b)
# x = random.randint(1, 5)
# print(x)
#  Give User 3 chances => if choice == x => You won  else

# random.randrange(start, stop, step)
# random.shuffle(list)
# random.choice(list)
# .........................................................................
# Pickle Module

# import pickle

# d = {"name": "Sam", "age": 23, "subjects": ["Maths", "English", "Science"]}

# with open("modules/data.pkl", "wb") as f:
#     pickle.dump(d, f)
#     print("Data Saved!....")

# wb => write in binary
# rb => read the binary

# with open("modules/data.pkl", "rb") as f:
#     x = pickle.load(f)
#     print("Data Loaded", x)
# ...............................................................
# Packages

# import mypackage, mypackage.math_utils, mypackage.string_utils

# from mypackage import *

# x = math_utils.pow(4, 2)
# # y = string_utils.rev("Danny")
# print(x)
# ................................................
# import mypackage
# x = mypackage.pow(3, 2)
# y = mypackage.rev("Bob")

# ...............................................
# from mypackage import rev,pow

# x = pow(3, 2)
# y = rev("Bob")
# print(x, y)
# ...............................................
