# print("Hello... World!....")

# Single line Comment
# print(56)


# Multi line comment
"""
print("Hello... World!....")
print(56.09)
"""
# .......................................................
# Rules to give variable names
# x = 34
# X = 56
# y = "Hello World!...."
# z = "Rohit"
# print(x, y, z, X)
# a1 = "Hi"
# _1a = "Hi2"

# # Age of a person
# age_of_person = 56
# # class=56
# print(x, age_of_person, z, X, _1a)
# ........................................................

# Correct the following invalid variable names and explain why they’re invalid:

# 1st_name = "Raj"
# class1 = "B.Tech"
# full_name = "Raj Kumar"
# print(1st_name, class, full-name)


# ...............................................................................

# Convert the following into valid multi-word variable names:

# total_marks_of_student=5687
# isstudent-present-today=True
# Average-Score=89

# ...............................................................................
"""
Task to print the following information
- Name 
- Age
- Gender 
- Salary 
"""

# age = 34
# name = "Sam"
# salary = 45000.50
# isRegular = True

# formatted string
# print(f"My Name is {name}. I am {age} year old. My salary is {salary}.")
# type() => function to check the data type of a variable
# print(type(age))
# print(type(name))
# print(type(salary))
# print(type(isRegular))

# -----------------------------------------------------------------------
"""
Personal Introduction with Data Types
Write a Python program that stores your name, age, and 
favorite hobby in variables.
Then:
Use the type() function to print the data type of each variable.
Print a sentence that introduces yourself using these variables.
"""


x = 34
print(type(x))  # int
x = "Hello!..."
print(type(x))  # string

salary = 45000
print(type(salary))
newSalary = float(salary)
print(type(newSalary), newSalary, salary)


new2salary = int(newSalary)
print(type(new2salary), new2salary)
age = -89
print(str(age), type(str(age)))
# bool() => other than 0 all integers return True.
print(bool(age), type(bool(age)))
name = ""
print(bool(name), type(bool(name)))
