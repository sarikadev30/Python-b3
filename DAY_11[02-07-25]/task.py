# Open and Closing of file
# file = open("data.txt", "r")  # opens data.txt in read mode
# print(file.read())

# file.close()

# with open("data.txt", "r") as f:
#     content = f.read()

#     print(content, f.tell())

# File is automatically closed after the with-block ends

# .........................................................................
# File Modes
# r => default
# w  => overwrites
# a => append
# variants of read and write
# r+ => read & write
# w+ => read & write
# a+ => read & write
# .....................................................................
# name
# age
# with open("file.txt", "w") as f:
#     f.write("We are in python session.")

# r+
# with open("data.txt", "r+") as f:
#     content = f.read()
#     # print(f.tell())
#     f.seek(10)
#     f.write("11th")
#     # print(content)

# w+
# with open("d2.txt", "w+") as f:
#     f.write("Hi.....")
#     f.seek(0)
#     content = f.read()
#     print(content)

# Hi.....

# a+
# with open("d2.txt", "a+") as f:
#     f.write("Sam...")
#     f.seek(0)
#     print(f.read())

# r+ w+ a+
# ...............................................
# read()
# readline()
# readlines()
# with open("d2.txt", "r+") as f:
#     l = f.readlines()
#     f.seek(0)
#     for i in l:
#         f.write(f"Good Morning...{i}")

# .........................................................

# with open("d2.txt", "r+") as f:
#     l = f.readlines()
#     f.seek(0)
#     for i in range(len(l)):
#         f.write(f"Good Morning...{l[i]}")
#         if i == 4:
#             f.seek(0)
#             print(f.read())
#             break

# ....................................................................
# with open("d2.txt", "r+") as f:
#     l = f.readlines()
#     f.seek(0)
#     for i in range(len(l)):
#         if i == 4:
#             f.seek(0)
#             print(f.read())
#             continue
#         f.write(f"Good Morning...{l[i]}")

# i=0    GM
# i=1    GM
# i=2    GM
# i=3    GM
# i=4      =>  four values will print
# i=5    GM
# .....
# ...........................................................
# with open("nums.txt", "r+") as f:
#     l = f.readlines()
#     sumR = 0
#     for i in range(len(l)):
#         sumR += int(l[i])
#     ans = sumR / len(l)
#     print(ans)

#     f.write(f"Sum of Above Numbers: {sumR} Average is {ans}")
# ...........................................................
