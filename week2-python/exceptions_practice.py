from timeit import timeit

# numbers = [1, 2]
# print(numbers[3])


# Handling exceptions
# Cleaning up

# try:
#     file = open("exceptions_practice.py")
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError) as ex:
#     print("You didn't enter a valid age.")
#     print(ex, type(ex))
# # except ZeroDivisionError as xe:
# #     print("Age cannot be zero")
# #     print(xe, type(xe))
# else:
#     print("No exeptions were thrown.")
# finally:
#     file.close()

# The with statement
try:
    with open("exceptions_practice.py") as file:
        print("File opened")

    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError) as ex:
    print("You didn't enter a valid age.")
    print(ex, type(ex))
# except ZeroDivisionError as xe:
#     print("Age cannot be zero")
#     print(xe, type(xe))
else:
    print("No exeptions were thrown.")

# Raising exceptions

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age

xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""

print(timeit(code1, number=10000))
print(timeit(code2, number=10000))
