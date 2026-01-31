# ---------------------------- Homework / Practice ----------------------------------

# Try these exercises to reinforce what you've learned:
# 1. Create variables for your name, age, and favourite_hobby
name = "Naresh Bohara"
age = 23
favourite_hobby = "watching series"
print(f"Hello! My name is {name}, I am {age} years old and my favourite hobby is {favourite_hobby}.")
# 2. Print them in one sentence using the + operator.
print(name + " " + str(age) + " "+ favourite_hobby)
# 3. Create two numeric variables and try different arithmetic operations.
num_1 = 22
num_2 = 4
print(num_1+num_2)
print(num_1-num_2)
print(num_1*num_2)
print(num_1/num_2)
print(num_1//num_2)
print(num_1%num_2)
print(num_1**num_2)

# 4. Use type() to check the data type of each variable.
print(type(name))
print(type(age))
print(type(num_1/num_2))
print(type(True))

# 5. Try converting between data types (e.g., int(), str(), float())
age_str = str(age)
print(type(age_str))

num_str = int("324")
print(type(num_str))

age_float = float(age)
print(age_float)

# flag = bool("324")
# print(flag)

bool("True")   # True (string → bool, not logical parsing)
bool("False")  # True (still string)

value = "true"
flag = value.lower() == "true"
print(flag)
