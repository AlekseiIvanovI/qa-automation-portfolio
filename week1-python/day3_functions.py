def greet(name):
    # quick welcome message at test start
    print(f"Welcome back {name}")


greet("Aleksei")


def greet2(first, last):
    # full name version – for logs and reports
    print(f"Welcome back {first} {last}")


greet2("Aleksei", "Ivanov")


def greet3(first, last):
    # returns string so I can save it or use in Allure
    return f"Welcome back {first} {last}"


message = greet3("Aleksei", "Ivanov")
file = open("name.txt", "w")
file.write(message)          # save test run info to file
file.close()


def increment(number, by):
    # simple counter – used in retry loops and timeouts
    return number + by


result = increment(10, 15)
print(result)
print(increment(10, 15))


def increment2(number, by=2):
    # default value 2 – perfect for retry count
    return number + by


print(increment2(10))        # uses default
print(increment2(10, 5))     # override when needed


def multiply(*numbers):
    # *args – multiply any number of values (pricing tests, etc.)
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))


def save_user(**user):
    # **kwargs – handle dynamic test data / API payload
    print(user)              # {'id': 1, 'name': 'John', 'age': 22}


save_user(id=1, name="John", age=22)


def save_user2(**user):
    # grab only what I need from payload
    print(user["id"])


save_user2(id=1, name="John", age=22)


def fizz_buzz(input):
    # classic validation logic – clean if/elif
    if (input % 5 == 0) and (input % 3 == 0):
        print("fizz_buzz")
    elif input % 3 == 0:
        print("Fizz")
    elif input % 5 == 0:
        print("Buzz")
    else:
        return input


print(fizz_buzz(7))
