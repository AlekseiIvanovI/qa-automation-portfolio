# Mad Libs Generator
def mad_libs_gen():
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    adverb = input("Enter an adverb: ")
    print(f"{noun} {verb} {adjective} {adverb}")


# mad_libs_gen()


# Password Strength check
def passw_str():
    while True:
        password_input = input("Enter a password: ")
        errors = []
        if len(password_input) < 8:
            errors.append("At least 8 characters long")

        has_lower = False
        has_upper = False
        has_digit = False

        for char in password_input:
            if char.islower():
                has_lower = True
            if char.isupper():
                has_upper = True
            if char.isdigit():
                has_digit = True

        if not has_lower:
            errors.append("At least one lowercase letter required")
        if not has_upper:
            errors.append("At least one uppercase letter required")
        if not has_digit:
            errors.append("At least one digit required")

            # Final result
        if not errors:
            print("Strong password accepted!")
            break
        else:
            print("Weak password! Missing:")
            for error in errors:
                print("•", error)
            print("Try again!\n")


# passw_str()


# Temperature Converter
def temp_conv():
    while True:
        temp = input("Enter temperature (or 'quit' to exit): ")
        if temp.lower() == "quit":
            print("Goodbye!")
            break
        while True:
            unit = input("In what unit: ").strip().upper()
            if unit in ["C", "F", "K"]:
                break
            print("Select between C F or K")
        temp = float(temp)

        if unit == "C":
            conv_f = temp * 9/5 + 32
            conv_k = temp + 273.15
            print(temp, unit + " = ", conv_f, conv_k)
        if unit == "F":
            conv_c = (temp - 32) * 5/9
            conv_k = temp + 273.15
            print(temp, unit + " = ", conv_c, conv_k)
        if unit == "K":
            conv_c = temp - 273.15
            conv_f = temp * 9/5 + 32
            print(f"{temp}, {unit} + \" = \", {conv_c}, {conv_f}")


# temp_conv()


# Grade Calculator
def grade_calc():
    while True:
        grade = input("Input your number: ")
        if grade == "quit":
            break
        grade = float(grade)
        if grade >= 90 and grade <= 100:
            print(f"{grade} -> you got an A!")
            break
        elif grade >= 80 and grade <= 89:
            print(f"{grade} -> you got an B!")
            break
        elif grade >= 70 and grade <= 79:
            print(f"{grade} -> you got an C!")
            break
        elif grade >= 60 and grade <= 69:
            print(f"{grade} -> you got an D!")
            break
        elif grade >= 0 and grade <= 99:
            print(f"{grade} -> you got an F!")
            break
        if grade >= 100 or grade < 0:
            print("Please select number in range 0 - 100")


# grade_calc()


# Ticket Price Calculator
def ticket_price():
    while True:
        age = input("Input your number: ")
        if age == "quit":
            break
        try:
            age = float(age)
        except ValueError:
            print("Please enter valid number")
        if age < 0:
            print("Age cannot be negative")
        elif age >= 0 and age <= 4:
            print(f"Age {int(age)} -> Ticket price: Free")
            # break
        elif age >= 5 and age <= 12:
            print(f"Age {int(age)} -> Ticket price: $10")
            # break
        elif age >= 13 and age <= 17:
            print(f"Age {int(age)} -> Ticket price: $15")
            # break
        elif age >= 18 and age <= 64:
            print(f"Age {int(age)} -> Ticket price: $25")
            # break
        else:
            print(f"Age {int(age)} -> Ticket price: $18")
            # break


# ticket_price()


# Simple Login System
def login_func():
    correct_pass = "python123"
    max_attempts = 3
    while True:
        user_input = input("Enter password: ")
        if user_input == "quit":
            print("Goodbye!")
            break
        if user_input == correct_pass:
            print("Login successfull!")
            break
        if user_input != correct_pass:
            max_attempts -= 1
            print("-" * 52)
            print(
                f"You have {max_attempts} attempt left before your account locked!")
            print("-" * 52)
            if max_attempts == 0:
                print("-" * 52)
                print(
                    f"Enter password: wrong 3 times -> Account locked!")
                print("-" * 52)
                break


login_func()
