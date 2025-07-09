# CALANDER MODULE

# import calendar

# x = calendar.month(2025, 7)
# y = calendar.calendar(2025)
# y = calendar.isleap(2004)
# y = calendar.leapdays(2000, 2015)  # 2000 2004 2008 2012
# y = calendar.weekday(2025, 8, 6)
# =>  wednesday  => 0 => Monday
# y = calendar.monthrange(2025, 7)
# print(y)

# ..............................................................................
# Regular Expression => REGEX  => to search a pattern
# @gmail.co .in .org .com
# Hi!
# ##########
# re regex module
import re

text = "Hi!... nut net not number bring for nor sum same some dam kick"

d = ["Hi !.. Sai", "Hi !.. Danni", "Bye!.. Sam", "Hi ! Leo", "Bye ! Leo"]

# n.t => start => n ends with t any character
# x = re.search(r"n.t", text)
# x = re.findall(r"n.t", text)
# x = re.findall(r"s.m", text)

# Search => end with string , Pattern in between |  Match => start with string
# for i in d:
#     # x = re.match(r"^Hi", i)
#     x = re.search(r"ai$", i)
#     print(x)

# s = "My Number is 98116666 and 4567"
# print(re.findall(r"\d+", s))

# sr = "Phone Number : 9823232323"
# print(re.sub(r"\d", "#", sr))

# email = "test@gmail.com"  # .co # .in # .org
# x = "tes%t.we3@yahoo.com"
# notEmail = "dxfcgvhbjndfcgvhb"
# res = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z]+\.[a-zA-Z]{2,}"
# # res = r"^[a-zA-Z0-9.]"

# # print(re.match(res, email))
# if re.match(res, notEmail):
#     print("Yes.....")
# else:
#     print("No........")
# ..............................................................................

# OOPS
# Class => blue print  # Object => instance of the class
# Person => name , age  ,city fun => print all the things


# class Person:
#     # Class variables
#     name = "Sam"

#     def fun(self):
#         print("Hi!...User", f"Bye...{self.name}")


# #  Creating Object of Person class (instance of the class)
# x = Person()
# Y = Person()
# x.fun()
# Y.fun()


# class Person:
#     # Class variables
#     city = "NewYork"

#     def __init__(self, name):
#         self.name = name  # Instance Variables
#         print(f"Hi!....{name}, Welcome to {self.city}")

#     def fun(self):
#         print("Hi!...User", f"Bye...{self.name}")


# #  Creating Object of Person class (instance of the class)
# x = Person("SAM")
# x.fun()


# class Car:
#     wheels = 4

#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         print(f"Car: brand={brand} model={model} wheels={self.wheels}")

#     def fun(self):
#         print("Hi!...User", self.wheels, self.brand, self.model)


# x = Car("Nisan", "Leaf")
# x.fun()


# Class Inheritance


# class Animal:
#     def speak(self):
#         print("Hi!... I want to say something")


# class Dog(Animal):
#     def bark(self):
#         print("Woo!...")


# x = Dog()
# x.speak()
# x.bark()


# class Person:
#     def __init__(self, name):
#         self.name = name
#         # self.__salary = salary  # Private Variables
#         print("Parent Constructor", name)

#     def fun(self):
#         print("Hi!! I am Parent")

#     # def sal(self):
#     #     print(f"Hi! salary {self.__salary}")


# class Student(Person):
#     def __init__(self, name, age, city):
#         super().__init__(name)
#         self.age = age
#         self.city = city
#         print("Child Constructor", age, city, name)

#     def fun(self):
#         print("Hi!! I am Child")

#     @staticmethod
#     def add(a, b):
#         print(a + b)


# # y = Person("Sam", 4500)
# x = Student("Sam", 23, "NewYork")
# # y.fun()
# # x.fun()
# # x.sal()
# # y.sal()
# x.add(3, 5)


# class Student:
#     c = 0

#     def __init__(self, name):
#         Student.c += 1
#         self.name = name

#     @classmethod
#     def fun(cls):
#         return cls.c


# x = Student("Sam")
# Y = Student("Sam")
# print(Student.fun())
