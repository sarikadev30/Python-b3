#  LIST
# SLICING
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# print(thislist[-4:-1])
# print(thislist[:4])
# print(thislist[2:5])
# print(thislist[2:])

# vegetables = ["Tomato", "Beans", "Onion"]
# print(len(vegetables))


# Addition
# append
# insert
# extend

# a = [1, 2, 3, 4, 5]
# b = [19, 20, 30, 45, 67]
# print(a)
# a.append(6)
# print(a)
# a.insert(3, 9)
# print(b)
# a.extend(b)
# print(a)

# for i in range(len(a)):
#     print(i, a[i])

# for el in a:
#     print(el)

# Updating the List
# a[0] = 89
# print(a)

# PROBLEM 1 **Perform the following tasks :**
# 1. **Create list of superheroes**
# 2. **push 4 superheroes in the List**
# 3. **Print the List**

# LIST OPERATIONS => CRUD => C=> CREATE R=> READ U => UPDATION D=> DELETION

# DELETION
# pop(index)
# b = [19, 20, 30, 45, 67]
# print(b)
# print(b, b.pop(1))
# b.pop()
# print(b)

# remove(item)
# b = [19, 20, 30, 45, 67, 30, 30, 40, 30]
# print(b)
# b.remove(19)
# print(b)

# stationary = []
# stationary.extend(["pen", "pencil", "notebooks", "marker", "Eraser", "Sharpner"])
# print(stationary[len(stationary) - 1], len(stationary) - 1)
# print(stationary)
# stationary.remove("marker")
# print(stationary)
# stationary.pop(2)
# print(stationary)
# stationary.pop()
# print(stationary)


# movies = ["bahubali", "Spider-Man", "Iron Man", "Superman"]
# for i in range(len(movies)):
#     if i == 3:
#         break
#     print(movies[i])


# movies = ["bahubali", "Spider-Man", "Iron Man", "Superman", "Thor", "Avengers"]
# for i in range(len(movies)):
#     if i == 2 or i == 4:
#         continue
#     print(movies[i])

# arr = [45, 56, 89, 12, 100, 39]
# Average of the elements of the list

# INBUILT FUNCTIONS
# print(sum(arr))    Calculate Sum
# print(max(arr))    Calculate Max value in the list
# print(min(arr))    Calculate Min value in the list
# print(arr.index(56))  Calculate the index of the element


# arr = [45, 36, 89, 100, 99]
# max = arr[0]  # 45
# min = arr[0]  # 45
# 1 max=56
# 2 max=89
# 4 max=100
# 5

# for i in range(1, len(arr)):
#     if arr[i] > max:
#         max = arr[i]
#     if arr[i] < min:
#         min = arr[i]

# print(max, min)
# ......................................................................
# Spiral Pattern

"""
1  2  3  4  5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9

[
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0]
]
"""
n = 5
# matrix = []
# for i in range(n):
#     row = []
#     for j in range(n):
#         row.append(0)
#     matrix.append(row)
# print(matrix)

matrix = [[0] * n for i in range(n)]
# boundaries
left = 0
right = n - 1
top = 0
bottom = n - 1
num = 1

while top <= bottom or left <= right:
    # left to right
    # 1 2 3 4 5    => 0 1 2 3 4
    for i in range(left, right + 1):
        matrix[top][i] = num
        print(matrix[top][i])
        num += 1
    top += 1

    # top to bottom
    # 5
    # 6
    # 7
    # 8
    # 9
    for i in range(top, bottom + 1):
        matrix[i][right] = num
        print(matrix[i][right])
        num += 1
    right -= 1

    # right to left
    # 13 12 11 10
    for i in range(right, left - 1, -1):
        matrix[bottom][i] = num
        print(matrix[bottom][i])

        num += 1
    bottom -= 1

    # bottom to top
    #  14 15 16
    for i in range(bottom, top - 1, -1):
        matrix[i][left] = num
        print(matrix[i][left])
        num += 1
    left += 1

print(matrix)
"""
1  2  3  4  5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9

"""
#  top=0 bottom=4 right=4 left=0 num=1 n=5
# top<=bottom and left<=right

# 0<=4 0<=4
# left to right
#  0 to 4
# matrix[top][i]
#  matrix[0][0]=1   num=1+1=2
#  matrix[0][1]=2   num=2+1=3
#  matrix[0][2]=3   num=3+1=4
#  matrix[0][3]=4   num=4+1=5
#  matrix[0][4]=5   num=5+1=6
# i=5 => False not in range
# top=0+1=1

# top to bottom
# 1 to 4
# matrix[i][right]
# matrix[1][4]=6  num=6+1=7
# matrix[2][4]=7  num=8
# matrix[3][4]=8  num=9
# matrix[4][4]=9  num=10

# right=4-1=3

# right to left
#  3 to 0
# matrix[bottom][i]
# matrix[4][3]=10 num=11
# matrix[4][2]=11 num=12
# matrix[4][1]=12 num=13
# matrix[4][0]=13 num=14
# bottom=4-1=3

# bottom to top
# 3 to 1
# matrix[i][left]
# matrix[3][0]=14 num=15
# matrix[2][0]=15 num=16
# matrix[1][0]=16 num=17
#  left=0+1=1


#  left to right => 1 to 3
# top = 1
# bottom=3
