# What are variables?
# -> Variables are the containers for storing data values that can be referenced and manipulated throughout the program. They are created when we assign a value using the equal sign (=).

# Think of variables as labeled boxes where we can store different types of information that our program needs to remember.

# age = 23
# name = "Naresh"
# is_student = True

# Variable naming rules: 
# 1. Most start with letters or underscores.
# invalid: 1score, @name

# 2. Only letters, numbers, underscores are allowed .
# valid: user123, total_sum 

# 3. Case-sensitive
# Age, age, AGE are three different variables

# 4. Avoid Python Keywords
# Don't use: if, for, while, class, return, from , import, global, try, ....etc.

# ----------------------------
# Variables and assignment 
# ----------------------------

# Basic varibale assignment: 
name = "Naresh Bohara"
age = 23
is_student = True
weight = 55
print(f"Name: {name}, Age: {age}, Student: {is_student}, Weight: {weight}")

# Multiple assignment
x, y, z = 10, 20, 30
print(f"x={x}, y={y}, z={z}")

# Variable reassignment
counter = 0
counter = counter + 1
counter += 1  # Shorthand
print(f"Counter: {counter}")


### Data Types in python:
# Python provides various types of built-in datatypes to store different kinds of information. 

# 1. Numeric types:
# Integer (int)
age = 25
count = -10
binary = 0b1010     # Binary: 10
hex_num = 0xFF      # Hexadecimal: 255

# Float (float)
price = 19.99
scientific = 1.5e3  # 1500.0
pi = 3.14159

# Complex (complex)
z = 3 + 4j


### 2. Text Type
# String (str) - Immutable
name = "Naresh"
message = 'Hello World'
multiline = """Line 1
Line 2
line 3"""
print(multiline)
# String operations
full_name = "Naresh" + " " + "Bohara"  # Concatenation
repeated = "Hi" * 3               # Repetition: "HiHiHi"


### imp note:
# what are triple quotes (""" """) in Python?
# Triple quotes are used to create multiline string literals, mainly used as docstrings for documentation, not comments.
# A docstring is a string written as the first statement in a module, function, class, or method to describe its purpose.


# how to access a docstring?
def add(a, b):
    """Returns sum of two numbers"""
    return a + b
print(add.__doc__)


### Boolean type:
# Boolean (bool) - Only True/False
is_active = True
is_empty = False

# Truthy/Falsy values
bool(0)        # False
bool(1)        # True
bool("")       # False
bool("Hello")  # True
bool([])       # False
bool([1,2])    # True

### 4. Sequence Types:
# List [] - Mutable, Ordered
fruits = ["apple", "banana", "cherry"]
fruits[0] = "orange"  # ✅ Can modify
fruits.append("grape")

# Tuple () - Immutable, Ordered
coordinates = (10.5, 20.3)
# coordinates[0] = 15.0  # ❌ ERROR - immutable


### 5. Mapping Type:
# Dictionary {} - Key-Value pairs
student = {
    "name": "Naresh",
    "age": 23,
    "city": "Dhangadhi"
}
student["age"] = 23    # ✅ Can modify values


### 6. Set Types:
# Set {} - Unique, Unordered
unique_nums = {1, 2, 3, 3, 2, 2, 2}  # {1, 2, 3}
print(unique_nums)
# unique_nums.add(5)
# unique_nums.remove(2)         # can be done


even_nums = {2, 4, 6, 8, }
print(even_nums)

# FrozenSet - Immutable set
frozen = frozenset([1, 2, 3])
# frozen.add(4)   # Error


### 7. None Type:
# None - Represents absence of value
result = None
if result is None:
    print("No result yet")

### TYPE CONVERSION:
# 1. Explicit Type Conversion (Type Casting)
# Programmer does it manually

# String → Number
int("42")       # 42
float("3.14")   # 3.14

# Number → String
str(100)        # "100"
str(3.14)       # "3.14"

# Other conversions
list("hello")   # ['h', 'e', 'l', 'l', 'o']
tuple([1,2,3])  # (1, 2, 3)
set([1,2,2,3])  # {1, 2, 3}

# Boolean conversion rules
bool(0)         # False
bool(1)         # True
bool("")        # False
bool([])        # False
bool({})        # False
bool(None)      # False


# 2. Implicit Type Conversion (Automatic):
# Python does it automatically. Python converts smaller → larger / safer type to avoid data loss.

a = 5        # int
b = 2.5      # float
c = a + b
print(c)     # 7.5
print(type(c))  # <class 'float'>
# int → float (automatic)

### imp note: 
"10" + 5             # ❌ TypeError
int("10") + 5        # Correct way

# 3. Boolean Implicit Conversion (Truthiness):
# These automatically convert to False:
0, 0.0, "", [], {}, (), set(), None



# ---------------- Implicit vs Explicit Type Conversion ----------------
#
# Type       | Who Converts  | Example               | Result | Notes
# ---------- | ------------- | --------------------- | ------ | -----------------------------
# Implicit   | Python        | 5 + 2.5               | 7.5    | int → float automatically
# Implicit   | Python        | True + 4              | 5      | True treated as 1
# Implicit   | Python        | 10 / 2                | 5.0    | Division always returns float
#
# Explicit   | Programmer    | int("10")             | 10     | String → Integer
# Explicit   | Programmer    | float("3.14")         | 3.14   | String → Float
# Explicit   | Programmer    | str(100)              | "100"  | Number → String
# Explicit   | Programmer    | list("abc")           | ['a','b','c'] | String → List
# Explicit   | Programmer    | set([1,2,2,3])        | {1,2,3}| Removes duplicates
#
# --------------------------------------------------------------------

