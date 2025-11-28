import random
# Email Formatter
# first_name = input("Input: ")
# last_name = input("Input: ")
# print(f"{first_name}.{last_name}@company.com")

# # Price Formatter
# prices = [12.22, 3232.2, 87.12, 991.22, 43.12]
# for i in prices:
#     print(f"${i:,.2f}")

# # FizzBuzz Classic


# def FizzBuzz():
#     for num in range(1, 101):
#         if '3' in str(num):
#             print("Lucky")
#         elif num % 5 == 0 and num % 3 == 0:
#             print("FizzBuzz")
#         elif num % 3 == 0:
#             print("Fizz")
#         elif num % 5 == 0:
#             print("Buzz")


# FizzBuzz()

# # Number Guessing Game


# def guessGame():
#     rand_num = random.randint(1, 101)
#     print(rand_num)
#     attempts = 0
#     while True:
#         guess = int(input("\nYour guess: "))
#         if guess < rand_num:
#             attempts += 1
#             print("Too low try again", f"\nAttempt: {attempts}")
#         elif guess > rand_num:
#             attempts += 1
#             print("Too high try again", f"\nAttempt: {attempts}")
#         else:
#             print(
#                 f"Congratulations, you guess right, number of attempts: {attempts}")
#             if attempts <= 3:
#                 print("Not bad")
#             elif attempts >= 10:
#                 print("Soo bad")
#             break


# guessGame()

# # Calculator with args


# def calculate(total, *numbers, multiply=False):
#     if multiply:
#         for number in numbers:
#             total *= number
#     else:
#         for number in numbers:
#             total += number
#     return total


# calculate(1, 2, 3, 4, 5)


# # Flexible Greeting Function
# def greet(*names, sep=' and ', greeting='Hello'):
#     if not names:
#         return f"{greeting}"
#     names_joined = sep.join(names)
#     return f"{greeting} {names_joined}"


# print(greet("tomas", "charly", "sam"))


# Shopping Cart Total
def cart_total(**items):
    print("Cart Contents:")
    total = 0
    for item_name, price in items.items():
        print(f"  {item_name:10} : ${price:>5.2f}")
        total += price
    print("-" * 25)
    print(f"{'Total':>12} : ${total:>5.2f}")
    return total


cart_total(apple=1.5, banana=0.8, milk=3.0)
