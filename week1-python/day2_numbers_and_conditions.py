import math

x = 1
y = 1.1
z = 1 + 2j

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

x = 3
x = x + 3
x += 3


print(round(2.3))
print(abs(-2.9))
print(math.ceil(2.2))


x = input("X: ")
print(type(x))
y = int(x) + 1
print(f"x: {x},\ny: {y},\n Answer: {y}")


# Falsy values
# ""
# 0
# None

# Comparison operators
print(10 > 3)
print(10 < 3)

print(10 == "10")
print(10 != "10")

# Conditional statements
temp = 75
if temp > 75:
    print("It is hot")
elif temp < 75:
    print("It is cold")
else:
    print("It is crazy")
print("Done")

# Ternary operator
age = 22
# if age >= 18:
#     message = "Eligible"
# else:
#     message = "Not eligible"
# print(message)

message = "Eligible" if age >= 18 else "Not eligible"
print(message)

# Logical operators
high_income = True
good_credit = False
student = False

if (high_income or good_credit) and not student:
    print("Eligible for loan")
elif not high_income and not good_credit:
    print("Not eligible for loan")

# Short circuit evaluation
high_income = False
good_credit = True
student = False

if high_income and good_credit and not student:
    print("Eligible for loan")
elif not high_income or not good_credit:
    print("Not eligible for loan")

# Chaining comparison operators
age = 22
if age >= 18 and age < 65:
    print("eligible")

if 18 <= age < 65:
    print("eligible")


# For loops
for number in range(1, 4):
    print("Attempt", number, number * ".")

# For else
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Succesfull")
        break
else:
    print(f"Attempted {number} times and failed")

# Nested loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# Iterables
for x in "Python":
    print(x)

for x in [1, 2, 3, 4, 5]:
    print(x)

# While loops
# number = 100
# while number > 0:
#     print(number)
#     number //= 2


command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

# Infinite loop
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break


count = 0
for x in range(1, 10):
    if x % 2 == 0:
        count += 1
        print(x)
print(f"We have {count} even numbers")
