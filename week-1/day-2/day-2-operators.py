### ---------------------------- Operators in Python ------------------------------
# Operators allow you to perform operations on variables and values. Python provides several types of operators for different purposes

# 1. ARITHMETIC OPERATORS:
# Used to perform mathematical calculations

a = 15
b = 4

print(a + b)    # Addition → 19
print(a - b)    # Subtraction → 11
print(a * b)    # Multiplication → 60
print(a / b)    # Division → 3.75 (always float)
print(a // b)   # Floor Division → 3 (removes decimal)
print(a % b)    # Modulus → 3 (remainder)
print(a ** b)   # Exponentiation → 15^4 = 50625


### Operator Precedence (PEMDAS rule):
# 1. Parentheses ()
# 2. Exponents **
# 3. Multiplication *, Division /, //, %
# 4. Addition +, Subtraction -

result = 3 + 4 * 2 ** 2   # 3 + (4 * (2 ** 2)) = 19

# 2. COMPARISON (RELATIONAL) OPERATORS
# Used to compare values
# Always return Boolean (True / False)

x = 11
y = 20

x == y    # Equal to
x != y    # Not equal to
x > y     # Greater than
x < y     # Less than
x >= y    # Greater than or equal to
x <= y    # Less than or equal to

# Chain comparison (Python special feature)
print(10 < x < 30)    # True → x is between 10 and 30


# 3. LOGICAL OPERATORS
# Used to combine conditional statements
a = True
b = False

a and b   # True if BOTH are True
a or b    # True if ANY one is True
not a     # Reverses the boolean value

# Short-circuit evaluation:
# and → stops when False is found
# or  → stops when True is found

age = 25
has_license = True

can_drive = age >= 18 and has_license
has_discount = age < 12 or age >= 65
is_adult = not (age < 18)


# 4. IDENTITY OPERATORS (is / is not):
# Used to compare memory locations (object identity)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

list1 == list2   # True → values are same
list1 is list2   # False → different objects in memory
list1 is list3   # True → same object

# Best practice:
# Use `is` ONLY for None, True, False
result = None
if result is None:    # ✅ Correct
    pass


# 5. MEMBERSHIP OPERATORS (in / not in):
# Used to check presence of value in sequence

fruits = ["apple", "banana", "cherry"]

"banana" in fruits        # True
"orange" not in fruits    # True

# Works with strings also
"app" in "apple"          # True


# 6. BITWISE OPERATORS (Advanced):
# Work on binary (bits) level

a = 10   # 1010
b = 4    # 0100

a & b    # AND → 0
a | b    # OR  → 14
a ^ b    # XOR → 14
~a       # NOT → -11
a << 1   # Left shift → 20 (multiply by 2)
a >> 1   # Right shift → 5  (divide by 2)



# ======================= ASSIGNMENT OPERATORS =======================
# Assignment operators are used to assign and update values in a variable
# They make code shorter and more readable
# -------------------------------------------------------------------

x = 5          # Basic assignment
# x = 5

x += 3         # Add and assign
# Equivalent to: x = x + 3

x -= 2         # Subtract and assign
# Equivalent to: x = x - 2

x *= 4         # Multiply and assign
# Equivalent to: x = x * 4

x /= 2         # Divide and assign
# Equivalent to: x = x / 2
# Result is always float

x //= 2        # Floor divide and assign
# Equivalent to: x = x // 2

x %= 3         # Modulus and assign
# Equivalent to: x = x % 3

x **= 2        # Power and assign
# Equivalent to: x = x ** 2


# -------------------------------------------------------------------
# Example Program
# -------------------------------------------------------------------
num = 10

num += 5    # 15
num *= 2    # 30
num -= 10   # 20
num //= 2   # 10

print(num)
# -------------------------------------------------------------------


# -------------------------------------------------------------------
# NOTES:
# -------------------------------------------------------------------
# +=, -=, *= etc. improve readability
# They modify the variable in-place
# /= always converts result to float
# Commonly used in loops and counters
# ===================================================================


