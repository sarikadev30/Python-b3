# COLLECTIONS MODULE

# COUNTER
# from collections import Counter

# fruits = [
#     "apple",
#     "banana",
#     "mango",
#     "mango",
#     "mango",
#     "litchi",
#     "apple",
#     "banana",
#     "mango",
#     "litchi",
#     "litchi",
#     "litchi",
#     "litchi",
# ]

# fruitD = Counter(fruits)
# print(fruitD)
# # Most Common Element
# print(fruitD.most_common(3))
# # Add more elements to the list
# fruitD.update(["kiwi", "cherry", "apricot", "kiwi", "cherry", "kiwi", "cherry", "kiwi"])
# print(fruitD)
# ................................................................................................
# Problem
# x = """Atoms of radioactive elements can split. According to Albert Einstein, mass and energy are interchangeable under certain circumstances.
# When atoms split, the process is called nuclear fission. In this case, a small amount of mass is converted into energy.
# Thus the energy released cannot do much damage. However, several subatomic particles called neutrons are also emitted during this process.
# Each neutron will hit a radioactive element releasing more neutrons in the process.
# This causes a chain reaction and creates a large amount of energy.
# This energy is converted into heat which expands uncontrollably causing an explosion. Hence, atoms do not literally explode.
# They generate energy that can cause explosions."""

# print()
# ...........................................................................................................
# DEQUE
# from collections import deque

# stack => LIFO => last in first out  => [1,2,3,4,5,6,7]  => last => push  , last => pop
# queue => FIFO => First in First out => [1,2,3,4,5,6,7] => last => enqueue , first => dequeue

# deque => double ended queue => add from both end , delete from both end

# x = deque([1, 2, 3, 4, 5, 6, 7])
# print(x)
# # addition
# x.append(9)
# x.appendleft(10)
# print(x)
# yR = x.pop()
# yL = x.popleft()
# print(yL, yR, x)
# x.append([12300000000, 67000000, 45000, 23456])
# x.appendleft([12300000000, 67000000, 45000, 23456])
# x.extend([34, 67, 23, 17])
# x.extendleft([12, 13, 141, 123, 12334])
# print(x)
# .....................................................................................................
# DEFAULTDICT =>
# from collections import defaultdict

# d = defaultdict(list)
# # d["a"] += 1

# print(d, d["b"])

# # usecase
# students = [
#     ("Alice", "CSE"),
#     ("Bob", "ECE"),
#     ("Charlie", "CSE"),
#     ("David", "ME"),
#     ("Eve", "ECE"),
#     ("Frank", "ME"),
#     ("Grace", "CSE"),
# ]
# ................................................................................
# NAMEDTUPLE

# x = ("t", "y", "i", "s", "e", "r")
# from collections import namedtuple

# y = namedtuple("Student", ["name", "age", "city"])
# Teacher = namedtuple("Teacher", ["name", "age", "city"])
# b = y("Sam", 23, "Delhi")
# b1 = y("Sunny", 21, "New York")
# b2 = Teacher("Danny", 43, "Delhi")
# print(b, b1, b2, Teacher)
# ..............................................................................
# import time

# print(time.time())
# time delay
# print("Start")
# print(time.time())
# time.sleep(2)
# print("Hi..........")
# print("End")

# now = time.time()
# # print(time.ctime(now))
# # print(time.localtime(now))
# t = time.localtime(now)
# x = time.strftime("%H:%M:%S, %m-%Y-%d ", t)
# print(x)

# start = time.perf_counter()
# for i in range(5):
#     print(i)
#     time.sleep(1)

# end = time.perf_counter()

# print("time taken: ", end - start)
# ..........................................................................
# DateTime Module
# Works with Date and Time in Simple and complex ways

# from datetime import datetime, timedelta

# now = datetime.now()
# x = timedelta(days=2)
# duration = now - x
# # print(duration, x)

# print(now.strftime("%Y ,%m, %d"))
# dateNow = "2023-03-04"
# print(dateNow)
# x = datetime.strptime(dateNow, "%Y-%m-%S")
# print(x)
