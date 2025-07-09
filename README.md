# Introduction to Python, Variables and Data Types

## What is Programming?

The process of preparing an instructional program for a device (such as a computer).

## What are Programming Languages?

It acts as a middle-man or translator for translating a program into machine code.

## How do computers perform tasks?

- To perform any task, we need 2 things
  - **The language that computers understand**
  - **Programming Environment**

## Programming Environment➖

- A programming environment combines hardware and software and allows a developer to build applications.
- Developers typically work in **integrated development environments or IDEs**.
- These connect users with all the features necessary to write and test their code correctly.
- Different IDEs will offer other capabilities and advantages.
- Examples of IDEs ➖ **Visual Studio, NetBeans, Eclipse, IntelliJ**, etc.

## What is Python?

Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.

| Term              | Meaning                                                       |
| ----------------- | ------------------------------------------------------------- |
| Interpreted       | Executes code line-by-line, no need to compile                |
| Object-Oriented   | Supports class and object-based program structure             |
| High-Level        | Easy to read/write, abstracted from hardware                  |
| Dynamic Semantics | Variables don’t need types declared, type checking at runtime |

Created by Guido van Rossum in 1991 at CWI (Centrum Wiskunde & Informatica), Netherlands.

## General-Purpose Language

Python can be used for:

AI & Machine Learning

Data Science (Most popular choice!)

Web Development (Django/Flask frameworks)

Automation and Scripting

Famous Companies Using Python + Django:
YouTube, Spotify, Pinterest, Instagram, Dropbox

## Why the name “Python”?

Inspired by the BBC comedy “Monty Python’s Flying Circus”.
Guido wanted a name that was short, unique, and mysterious.

## Why Learn Python?

- Simple & Easy to Learn
- Dynamic and Powerful
- Huge Library Ecosystem (130,000+ packages)
- Free and Open Source
- Platform Independent
- Interpreted (no need to compile)
- Robust Exception Handling

## Indentation in Python

Python uses indentation to define blocks of code instead of curly braces {}.

```
    if True:
    print("This is indented correctly")
    ❌ Indentation error if not properly aligned.

```

---

## Note => The extension used for Python files is .py.

## Printing Output in Python

Use the built-in print() function:

```
    print("Hello, world!")
```

You can print strings, numbers, and variables.

## Python Comments

Used to explain code and prevent execution.

### Single-line comment:

```
# This is a comment
```

### Multi-line comment:

```
'''
This is
a multi-line comment
'''

```

## What is a Variable?

A named container to store data.

```
name = "Alice"
age = 25
```

Think of variables as boxes with labels.
(CASE SENSITIVE)

## Check Variable Type

```
print(type(name))   # <class 'str'>
print(type(age))    # <class 'int'>
```

Python is a fantastic language that automatically identifies the type of data for us.

## Rules for Declaring Variables

### Valid Names:

1. Must start with a letter or \_ (underscore)
2. Can contain letters, numbers, and underscores
3. Case-sensitive (age, Age, and AGE are different)

## Data Types in Python

<img src="./dataType.png" width="60%"/>

Can you store milk in a basket or can you use a bottle to store fruits?

We are using different types of containers to store different things.

While the bottle can hold milk or water or juice, it will hold only liquids.

Similarly,

- A variable of type **_string_** (like the variable - *custName*), can store only strings.
- A variable of type **int** (like the variable - *custAge)* can store only integers.
- A variable of type **boolean** (like the variable - *custMaritalStatus)* can store either true or false.
- A variable of type **float** (like the variable - fruitWeight*)* can store only decimal values.

*The type of data a variable can hold is called its* **Data type**.
It may be **int**, **string, boolean, float,** etc. (A variable of type Boolean can either be *True* or *False).*

| Data Type | Example         | Description     |
| --------- | --------------- | --------------- |
| `str`     | `"Alice"`       | Text values     |
| `int`     | `25`            | Whole numbers   |
| `float`   | `3.14`          | Decimal numbers |
| `bool`    | `True`, `False` | Logical values  |

## Type **Casting in Python**

Type Casting is the method to convert the variable data type into a certain data type in order to the operation required to be performed by users.

There can be two types of Type Casting in Python –

- Implicit Type Casting
- Explicit Type Casting

### Implicit Type Casting

In this, Python **converts the data type** into another data type **automatically**. In this process, users don’t have to involve in this process.

### Explicit Type Casting

In this, Python needs **user involvement to convert the variable data type** into a certain data type in order to the operation required.

Mainly type casting can be done with these data type functions:

- **int():** int() function take float or string as an argument and return int type object.
- **float():** float() function takes int or string as an argument and returns float type object.
- **str():** str() function take float or int as an argument and return string type object.
- **bool():** bool() function take float, string or int as an argument and return a boolean-type object. Number other than 0 change into True. Empty String change into False.

## Many Values to Multiple Variables

Python allows you to assign values to multiple variables in one line.

Ex➖

```
x,y,z= "box", "pencil", "eraser"

print(x)    # box
print(z)    # pencil
print(y)    # eraser
# The number of variables matches the number of values, or else you will get an error
```

## One Value to Multiple Variables

Python allows you to assign the *same* value to multiple variables in one line.

Ex➖

```cpp
a=b=c="Maggi"
print(a)    # Maggi
print(b)    # Maggi
print(c)    # Maggi
```

## Mathematical Operators

The mathematical operators in Python are :

- **Addition Operator**
- **Subtraction Operator**
- **Multiplication Operator**
- **Division Operator**
- **Modulo Operator** => gives the remainder
- **Exponentiation Operator** => compute the power of any number

## String Concatenation

- Concatenation means a series of interconnected things.
- Use **+** to join two or more string

```
  a="Hii...."
  b="Sam...."
  print(a+b)          # Hii....Sam....
```

## Comparison Operators

Comparison operators are used for comparing two values.

- There are 6 comparison operators:
  - **> (Greater Than)**
  - **>= (Greater Than Equal To)**
  - **< (Less Than)**
  - **<= (Less Than Equal To)**
  - **== (Equal)**
  - **!= (not Equal)**
- The result of a comparison operator is always a boolean value.

## Logical Operators

A logical operator is a symbol or word used to connect two or more expressions.

## Types of Logical Operators

Python provides three logical operators:

1. and
2. or
3. not

## Assignment Operators

Assignment operators are used to assign values to variables.

- The most common is `=`, which assigns the right-hand side value to the left-hand side variable.
- Python also supports compound assignment operators.

### Types of Assignment Operators:

| Operator | Description             | Example          |
| -------- | ----------------------- | ---------------- |
| =        | Assign value            | a = 5            |
| +=       | Add and assign          | a += 2 (a = a+2) |
| -=       | Subtract and assign     | a -= 2 (a = a-2) |
| \*=      | Multiply and assign     | a *= 3 (a = a*3) |
| /=       | Divide and assign       | a /= 2 (a = a/2) |
| %=       | Modulo and assign       | a %= 2 (a = a%2) |
| //=      | Floor divide and assign | a //= 2          |
| \*\*=    | Exponent and assign     | a \*\*= 2        |

## Membership Operators

Membership operators are used to test whether a value is a member of a sequence (like string, list, tuple, etc.).

### Types of Membership Operators:

| Operator | Description                 |
| -------- | --------------------------- |
| in       | Returns True if present     |
| not in   | Returns True if not present |

### Note: Membership checks are case-sensitive.

## Identity Operators

Identity operators compare memory locations (i.e., whether two variables point to the same object).

### Types of Identity Operators:

| Operator | Description                          |
| -------- | ------------------------------------ |
| is       | Returns True if objects are same     |
| is not   | Returns True if objects are not same |

```python
a = 100
b = 100
print(a is b)

x = "hello"
y = "hello"
print(x is y)

z = "hello world"[0:5]
print(x == z)
print(x is z)

```

```
a = [1, 2]
b = a
c = [1, 2]

print(a is b)       # True (same memory)
print(a is c)       # False (different memory)
print(a == c)       # True (same values)
```

```python
num1 = 256
num2 = 256
print(num1 is num2)       # True (cached)

name1 = "Python"
name2 = "Py" + "thon"
print(name1 is name2)     # True (interned string)
```

```
x = 100
y = 100
z = 101

print(x is y)       # True (in small integer range cache)
print(x is not z)   # True
```

### Note:

- `is` checks memory identity, not just value.
- Use `==` for equality and `is` for identity.

### Understanding Caching and Interned Strings

**What is it?**

Caching is an optimization technique where **Python reuses objects** instead of creating new ones every time—this saves memory and increases performance.

### 1. Integer Caching:

- Python automatically **caches integers from -5 to 256**.
- This means when you assign `a = 100` and `b = 100`, **both point to the same memory location**.
- Python **caches small integers** in the range `5` to `256`.
- These integers are pre-allocated and shared to improve performance.
- When you assign values in this range, Python reuses the existing object instead of creating a new one.

```
a = 100
b = 100
print(a is b)  # True → both point to the same memory location
```

- But outside this range, integers are not guaranteed to be cached:

```
x = 300
y = 300
print(x is y)  # False → different memory locations
```

### 2. Interned Strings:

**What is string interning?**

Interning means Python stores only **one copy of some strings** (like literals or identifiers) to **save memory** and make comparisons faster.

### Automatic Interning:

When you create two **identical string literals**, Python stores them **in the same memory**.

Identical strings created as **literals** are often stored in the same memory.

```
s1 = "hello"
s2 = "hello"
print(s1 is s2)  # True → interned string
```

## Conditional Statements

Conditional Statements in Python perform different computations or actions depending on whether a specific Boolean constraint evaluates to true or false.

- Conditional statements are used **to decide the flow of execution based on different conditions**. If a condition is true, you can perform one action and if the condition is false, you can perform another action.
- Through Conditional Statements, we can control which code needs to run or which code will not run.

For Example: the traffic light controls the flow of vehicles on the road.

- Depending upon the color of the light, the actions happened.
- If the light is green, then it is a signal to move.
- If the light is red then it is a signal to stop.

## Different Types of Conditional Statements

There are four types of conditional statements in Python.

1. If statement
2. If…Else statement
3. If…Elif…Else statement
4. Nested If

### If - Statement

```
name1 = "Rahul"
name2 = "Rahul"
check = (name1==name2)

if(check):
  print("Both Names are same")

```

## Ternary Operator

- Ternary operators also known as **conditional expressions** are operators that evaluate something based on a condition being true or false.
- It was added to Python in version **2.5.**
- It simply allows testing a condition in a **single line** replacing the multiline if-else making the code compact.
- Syntax➖
  ```
  [on_true] if [expression] else [on_false]
  ```
- For ex-

  ```
  # to check whether a number is odd or even
  a=10;
  print("Even Number") if(a%2==0) else print("Odd Number");

  x = 5
  result = "Greater" if x > 10 else "Equal" if x == 10 else "Less"
  print(result)
  ```

## WHILE LOOP

```
  starting_point  # called as initialization

  while(till_when_he_will_jump):     # condition to terminate the loop

	# operation that is to be performed

	how_many_jump_at_a_time          # Increment/decrement
```

### Break

- **Break** means to come out of the loop and stop the execution.

### Continue

- **Continue** is basically saying go back to the condition.

## The else Statement with While in Python

With the else statement we can run a block of code once when the condition no longer is true:

```python
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
```

## FOR LOOP

## NESTED LOOPS

## DATA TYPES

### 1. Primitive Data Types (also called basic or built-in types)

These are the most **basic types of data**, directly supported by the Python language.

| Data Type | Description                      | Example         |
| --------- | -------------------------------- | --------------- |
| `int`     | Integer numbers                  | `10`, `-5`, `0` |
| `float`   | Decimal (floating point) numbers | `3.14`, `-0.1`  |
| `bool`    | Boolean values (True or False)   | `True`, `False` |
| `str`     | Text (string of characters)      | `"Hello"`       |

> **Note:** These are immutable (cannot be changed after creation).

---

### 2. Non-Primitive Data Types (also called complex or user-defined types)

These are built using primitive types.
They can store **multiple values** and offer **more functionality**.

| Data Type         | Description                     | Example                 |
| ----------------- | ------------------------------- | ----------------------- |
| `list`            | Ordered, mutable collection     | `[1, 2, 3]`             |
| `tuple`           | Ordered, immutable collection   | `(1, 2, 3)`             |
| `set`             | Unordered, unique items         | `{1, 2, 3}`             |
| `dict`            | Key-value pairs                 | `{"name": "Sam"}`       |
| `array`           | Like lists, from `array` module | `array('i', [1, 2, 3])` |
| `class`, `object` | Custom types defined by user    | OOP structures          |
| `function`        | Callable object                 | `def greet(): ...`      |

## What are Mutability and Immutability

## Mutability

In Python, mutability means you can directly modify an object after the creation
. For example, a list is a mutable object. After creating a list, you can add, modify, or remove elements from it.

## Immutability

In Python, immutability means you cannot directly modify an object after the creation
. For example, Tuple is an immutable object. After creating a tuple, you cannot add, modify, or remove elements from it.

## Sets

- Sets are used to store multiple items in a single variable.
- Sets are declared using { } without a colon.
- Set items are unordered (which means that the items in a set do not have a defined order), unchangeable (meaning that we cannot change the items after the set has been created), and do not allow duplicate values.
- No fetching possible (No Indexing and Slicing)
- We can add or delete the data.
- Data within the sets are automatically sorted.
- They contain only unique data. (**Data Duplication not possible**)
- **Syntax ⇒ `{** item1,item2, item3, ... }`
- **Example➖**
  ```python
  s={1,3,4,5,8}
  print(s)           # {1, 3, 4, 5, 8}
  print(type(s))     # <class 'set'>
  ```
- Since Sets consist of sorted and unique data, searching for a particular element within the set is very quick.

## Tuples

- Sibling of List
- **Immutable Data Object** ➖ Once you create the tuple, you can’t manipulate it. (no addition, deletion, or replacement)
- We can
  - Create Tuple
  - Indexing and Slicing
  - Create a new tuple by merging two or more tuples.
- A safer option for data collection
  - **Example** ⇒ Students’ marks if stored in a list manipulation can be possible (as addition, deletion, and changes are applicable) but Tuple is **immutable** hence, safer than a list
- When the objective is to collect the data and has no further objective of editing it ⇒ **Use TUPLE**

## Dictionary

- Python dictionary is an **ordered collection of items**.
- As of Python version 3.7, dictionaries are *ordered*. In Python 3.6 and earlier, dictionaries are *unordered*.
- Dictionaries are **optimized to retrieve values when the key is known.**
- A dictionary is a collection that is **changeable** and **does not allow duplicates**.
- Dictionaries are written **with curly brackets** and **have keys and values.**
- Holds data as **`key-value`** pair
- No concept of an index system and hence they are unordered.
- To fetch the data we use keys.
- A dictionary can’t have two keys with the same name. [ **keys must be unique and values can repeat**]
- Dictionaries are mutable, so we can
  - add a new key-value pair
  - replace the value not a key
  - delete a key-value pair
- **Syntax**➖
  ```python
  dict={
  	"key1": value,
  	"key2": "value",
  }
  ```

While the values can be of any data type and can repeat, keys must be of **immutable type (string, number, or tuple with immutable elements) and must be unique**.

## Functions

A block of code designed to perform a particular task; they are very useful in making code simplified and manageable.

```
  def channel_1():
      x="Sam";
      print(x);

  channel_1()
  channel_1()
  channel_1()
  channel_1()
```

### Default Arguments

### Variable-Length Arguments

### Keyworded Arguments => Arguments passed as name=value.

## Scope of Variables

### Local Scope

```
def greet():
    message = "Hello"
    print(message)  # message is local to this function

greet()
# print(message)  # Error: message is not defined
```

### Enclosing Scope (Nonlocal)

An enclosing scope refers to the scope of a function that contains another nested function.
Variables in this outer function are not local to the inner function, but they are not global either — they’re in the enclosing scope.

To access and modify a variable from an enclosing scope inside a nested function, we use the nonlocal keyword.
Without nonlocal, Python would treat message in inner() as a new local variable.

```
	def outer():
    msg = "Hello"

    def inner():
        nonlocal msg
        msg = "Hi"
        print("Inner:", msg)

    inner()
    print("Outer:", msg)

	outer()

```

### Global Scope

```
x = 10  # Global variable

def print_x():
    print(x)

print_x()
```

If modifying global:

```
x = 5

def change():
    global x
    x = 10

change()
print(x)  # Output: 10
```

### Built-in Scope

The built-in scope contains the names of all built-in functions, exceptions, and objects provided by Python. These are always available unless shadowed.

These come from the **builtins** module, and examples include:

```
  len()

  type()

  print()

  max(), min()

  sum()
```

Exception, ValueError, etc.

Python looks for a variable in this order: Local → Enclosing → Global → Built-in
print(len("Python")) # 'len' is a built-in function

## Python Exception

Exceptions are runtime errors that occur when a program encounters something unexpected or invalid during execution.
Instead of crashing the program, Python allows us to handle these exceptions

```
  print(10 / 0)
```

### Why Exceptions Happen ?

- File not found
- Invalid input
- Dividing by zero
- Accessing an index that doesn’t exist
- Working with wrong data types

### Benefits of Using Exceptions:

- Prevents program from crashing
- Improves user experience with meaningful error messages
- Helps in debugging

### try-except block

Used to catch and handle exceptions that occur in a block of code to prevent program crash.

```
  try:
    a = 10 / 0
  except ZeroDivisionError:
    print("Cannot divide by zero!")

```

### Multiple except blocks

To handle different types of exceptions separately with custom responses.

```
try:
    num = int("abc")
except ValueError:
    print("Invalid conversion to int")
except ZeroDivisionError:
    print("Zero division")
```

### Catching multiple exceptions together

To catch multiple related exceptions using a single except clause.

```
try:
    # Some code
    pass
except (ValueError, ZeroDivisionError) as e:
    print("Caught exception:", e)
```

### Generic exception handling

Catch any kind of exception, useful when the exact exception type is unknown.

```
try:
    x = 10 / 0
except Exception as e:
    print("Error occurred:", e)
```

### finally block

Code in finally always runs — whether or not an exception occurs.

```
try:
    f = open("sample.txt")
except FileNotFoundError:
    print("File not found.")
finally:
    print("This block always runs.")
```

### Raising exceptions

To manually trigger an exception when a specific condition is violated.

```
  def divide(a, b):
      if b == 0:
          raise ValueError("b cannot be zero")
      return a / b

  divide(10, 0)
```

### User-defined exceptions

```
class NegativeAgeError(Exception):
    pass

age = -2
if age < 0:
    raise NegativeAgeError("Age cannot be negative")
```

## File Handling

### Files

- Files are a way to store data permanently on your computer.
- Python can open files, read their contents, write new information, and close them when done.
- Files can be text-based (like `.txt`), or more structured formats like `.csv`.

**Key Concepts:**

- **Opening a file:**
  Before reading or writing, we must open a file.
- **Closing a file:**
  After finishing with file operations, we close it, so the system knows we’re done and all changes are saved.
- **File Modes:**
  Determine how we interact with the file (read-only, write-new, append, etc.)

---

### Need of Files

If you need to store large amounts of data, user preferences, or logs, relying on variables isn’t enough. Files let you:

- Preserve data after the program ends.
- Share data between different runs of your program.
- Process bigger data sets that you can’t hard-code into variables.

```
  file = open("data.txt", "r")  # opens data.txt in read mode
  print(file)


  file.close()  # close the file after finishing
```

```
  with open("data.txt", "r") as f:
    content = f.read()
    print(content)
  # File is automatically closed after the with-block ends
```

## Locating Modules in Python

When you import a module in Python using import module_name, Python looks for that module in a sequence of directories. This sequence is stored in the list sys.path.

### What is sys.path?

sys.path is a list of directory paths that Python interpreter searches through when trying to locate a module you want to import.

It is defined in the sys module, so you must import sys to access it.

Python follows this order:

- Looks in the current directory ('')

- Then in site-packages (user or system installed)

- Then in standard library paths

- If not found, it raises a ModuleNotFoundError

### Adding Custom Paths

You can also manually add paths to sys.path at runtime:

```
import sys
sys.path.append('/my/custom/module/path')
import mymodule
```

This is useful if:

- You have a shared module in a separate directory.
- You want to avoid moving files around.

## What is `pickle` in Python?

Imagine you have a Python object (like a list, dictionary, or even a custom class), and you want to **save it to a file** so that you can **use it later** — maybe even after restarting your program or computer.

That's where the `pickle` module comes in.

## Why Use Pickle?

- To **store data permanently** (like saving app state, ML models, game progress, etc.)
- To **transfer Python data** between different scripts or machines

---

## 🔧 Two Main Functions

| Function        | Purpose                                |
| --------------- | -------------------------------------- |
| `pickle.dump()` | Save (serialize) Python object to file |
| `pickle.load()` | Load (deserialize) object from file    |

## Python Packages

A package is a directory containing a special **init**.py file (can be empty) and multiple modules. Packages help organize modules in a hierarchical way.

Structure Example:

```
  mypackage/
├── **init**.py
├── math_utils.py
└── string_utils.py
```

Use Case: Encapsulate related modules for better structure and reuse.

### **init**.py

is a special Python file used to indicate that a directory is a Python package.

- Without it (in Python versions < 3.3), the directory wouldn’t be recognized as a package.

- In modern Python (≥ 3.3), it’s optional, but still widely used for:

  - Package initialization

  - Controlling what gets imported

  - Organizing internal logic

```
  # math_utils.py
def square(n):
    return n * n

# string_utils.py
def reverse(s):
    return s[::-1]

# main.py
from mypackage import math_utils, string_utils
print(math_utils.square(4))
print(string_utils.reverse("hello"))
```

## COLLECTION MODULE

The `collections` module provides alternatives to built-in containers like `dict`, `list`, `set`, and `tuple`. These are:

1. **Counter**
2. **deque**
3. **defaultdict**
4. **namedtuple**

## TIME MODULE

- Definition : The `time` module provides functions to work with time-related tasks such as delays, measuring execution time, and formatting time and dates.
- **Use Cases:**
  - Add delays in programs (e.g., games, loaders)
  - Benchmark how long code takes to run
  - Format and display current time
- **Commonly Used Functions**
  | Function | Description |
  | -------------------------- | -------------------------------------------------- |
  | `time.time()` | Returns current time in seconds since epoch |
  | `time.sleep(seconds)` | Suspends execution for the given number of seconds |
  | `time.ctime([secs])` | Converts time in seconds to a readable string |
  | `time.localtime([secs])` | Converts time to local time struct |
  | `time.strftime(format, t)` | Formats a struct_time as a string |
  | `time.perf_counter()` | High-resolution performance timer |
- **Epoch** in Python (and Computers)
  The **Epoch** is a fixed point in time used as a reference for measuring time in computing.
  In most systems (including Python), **Epoch time** is:
  > January 1, 1970, at 00:00:00 UTC
  > This is also known as **Unix Time** or **POSIX Time**.
- Difference between localtime() and ctime()
  | Feature | `time.localtime()` | `time.ctime()` |
  | ---------------------- | -------------------------------------- | ------------------------------- |
  | **Returns** | `time.struct_time` (tuple-like object) | String |
  | **Readable?** | No (raw object) | Yes (formatted time string) |
  | **Can extract parts?** | Yes (year, hour, etc.) | No (need parsing) |
  | **Use Case** | When you want to **manipulate time** | When you want to **print time** |

## DATE TIME MODULE

The `datetime` module provides classes to **work with dates and times** in both simple and complex ways. It is part of Python’s standard library.

---

## REGEX MODULE

### **Core Functions of `re` Module**

| Function       | Description                            |
| -------------- | -------------------------------------- |
| `re.search()`  | Searches for the first match           |
| `re.findall()` | Returns a list of all matches          |
| `re.match()`   | Checks for a match at the **start**    |
| `re.sub()`     | Replaces pattern with something else   |
| `re.compile()` | Compiles a pattern into a regex object |

---

## **Basic Regex Patterns (Metacharacters)**

| Pattern | Meaning                            | Example Match                                  |
| ------- | ---------------------------------- | ---------------------------------------------- |
| `.`     | Any character except newline       | `"c.t"` → `cat`, `cut`                         |
| `^`     | Start of string                    | `"^Hi"` matches `Hi`                           |
| `$`     | End of string                      | `"bye$"` matches `goodbye`                     |
| `*`     | 0 or more repeats                  | `"go*gle"` matches `ggle`, `google`, `gooogle` |
| `+`     | 1 or more repeats                  | `"lo+l"` → `lol`, `lool`                       |
| `?`     | 0 or 1 repeat                      | `"colou?r"` matches `color`, `colour`          |
| `{n}`   | Exactly n times                    | `"a{3}"` → `aaa`                               |
| `{n,m}` | Between n and m times              | `"a{2,4}"` → `aa`, `aaa`, `aaaa`               |
| `[]`    | Matches a set of characters        | `"[aeiou]"`                                    |
| `\d`    | Digit (0–9)                        | `"a\d"` → `a2`                                 |
| `\D`    | Non-digit                          | `"\D"` matches `a`, `!`                        |
| `\w`    | Word character (a-z, A-Z, 0–9, \_) |                                                |
| `\s`    | Whitespace                         | `"Hello\sWorld"`                               |
| `       | `                                  | OR                                             |
| `()`    | Grouping                           | `"(ha)+"` → `ha`, `hahaha`                     |

---

## Python Threads

threading module allows you to run multiple threads (tasks) at once.

### Methods:

start(): Starts the thread.

run(): Defines the task to run.

join(): Waits for the thread to finish.

### Lock

Prevents multiple threads from modifying shared data simultaneously.

### Daemon Thread

Background thread that automatically exits when the main thread finishes.

### Timer

Delays execution of a function by a certain amount of time.

### GIL (Global Interpreter Lock)

Ensures only one thread executes Python bytecode at a time.

```
def task():
    print("Running")

t = threading.Thread(target=task)
t.start()
t.join()  # tells the main program to wait for thread t to finish before moving on.

```

## Python Queue

Used for thread-safe task queues.

### Types:

Queue() – FIFO (First-In, First-Out)

LifoQueue() – Last-In, First-Out

PriorityQueue() – Elements sorted by priority

### Methods:

put(): Add item.

get(): Remove item.

empty(): Check if empty.

task_done(): Signal task completion.

join(): Block until all tasks are done.

```
from queue import Queue

q = Queue()
q.put("A")
print(q.get())

```

## OS Interface

Interacts with the operating system.

Common Methods:

os.rename(src, dst) – Rename file or folder.

os.listdir(path) – List directory contents.

os.remove(path) – Delete file.

os.getcwd() – Get current directory.

os.chdir(path) – Change directory.

os.stat(path) – Get file info.

os.path.isdir() – Check if path is directory.

os.mkdir() – Make directory.

os.makedirs() – Make nested directories.

os.access(path, mode) – Check permission.

os.walk(path) – Generator for traversing directory trees.

os.system(cmd) – Execute system command.

os.popen(cmd) – Run command and get output.

os.environ – Access environment variables.

```
import os
print(os.getcwd())
os.system("echo Hello")
```

## Python Logging

Used to log events and errors.

### Levels:

**DEBUG:** Detailed info for diagnosis.

**INFO:** Confirmation that things are working.

**WARNING:** Something unexpected.

**ERROR:** Problem preventing function.

**CRITICAL:** Serious error.

```
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Information")
logging.error("An error occurred")
```

---

Happy Coding!........
