from collections import deque
from array import array
from sys import getsizeof

letters = ["a", "b", "c", "d"]
matrix = [[0, 1], [2, 3], [4, 5]]
zeros = [0] * 5
print(zeros)

combined = zeros + letters
print(combined)
numbers = list(range(20))
print(numbers)
chars = list("Hello World")
print(chars)
print(len(chars))

# accessing items
letters[0] = "R"
print(letters[0:])
print(letters[::2])

numbers_list = list(range(20))
print(numbers_list[::2])
print(numbers_list[::-1])

numbers2 = [1, 2, 3]
first = numbers2[0]
second = numbers2[1]
third = numbers2[2]
first, second, third = numbers2

numbers3 = [1, 2, 3, 4, 5, 6]
x, y, z, *other = numbers3
print(x, other)

x, *other, last = numbers3
print(x, last)
print(other)


letters2 = ["a", "b", "c"]
for letter in letters2:
    print(letter)

for letter in enumerate(letters2):
    print(letter)

# Add to an end of list
letters2.append("d")
print(letters2)

# Add to the beginning of list
letters2.insert(0, "-")
print(letters2)

# Remove item to end of the list
letters2.pop()
print(letters2)

# Remove item at the beginning of the list
letters2.pop(0)
print(letters2)


letters2.remove("b")
print(letters2)

del letters2[0]
print(letters2)

letters.clear()
print(letters2)

# Finding items
new_list = ["a", "b", "c", "d"]
print(new_list.count("a"))
if "a" in new_list:
    print(new_list.index("a"))

# Sorting items
list_numbers = [3, 12, 44, 2, 7, 8]
list_numbers.sort()
print(list_numbers)
list_numbers.sort(reverse=True)
print(list_numbers)
print(sorted(list_numbers))
print(sorted(list_numbers, reverse=True))

# Sorting lists
items = [
    ("Product 1", 70),
    ("Product 2", 25),
    ("Product 3", 33)
]


# def sort_item(item):
#     return item[1]


# items.sort(key=sort_item)
# print(items)

# # Lambda Functions
# items.sort(key=lambda item: item[1])
# print(items)

# # Map Function
# prices = []
# for item in items:
#     prices.append(item[1])
# print(prices)


map_price = map(lambda item: item[1], items)
for item in map_price:
    print(item)

prices = list(map(lambda item: item[1], items))
print(prices)


# Filter function
items = [
    ("Product 1", 70),
    ("Product 2", 25),
    ("Product 3", 33)
]

# filtered = list(filter(lambda item: item[1] > 33, items))
# print(filtered)
filtered = [item for item in items if item[1] > 33]
print(filtered)

# List comprehensions
prices = [item[1] for item in items]
print(prices)


# Zip function
list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(list(zip(list1, list2)))

# Stacks
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
remove_last = browsing_session.pop()
print(remove_last)
print(browsing_session)
print("Redirect to", browsing_session[-1])
if not browsing_session:
    print("Disable")

# Queues
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("Empty")

# Tuples
point = (1, 2, 3)
print(point)
print(point[0])
x, y, z = point
point2 = tuple("Hello World")
print(point2)

# Swapping Variables
c, m = 10, 11
c, m = m, c
print("c", c)
print("m", m)


# Arrays
nums = array("i", [1, 2, 3])
nums.append(4)
print(nums)

# Sets
nums2 = [1, 1, 2, 3, 4]
first = set(nums2)
print(first)
second = {1, 5}
print(first | second)
print(first & second)
print(first - second)
print(first ^ second)

if 1 in first:
    print("Yes")

# Dictionaries
dictionar = {"x": 1, "y": 2}
dictionar = dict(x=1, y=2)
dictionar["x"] = 10
dictionar["z"] = 12
print(dictionar)
if "a" in dictionar:
    print(dictionar["a"])
print(dictionar.get("a", 0))
del dictionar["x"]
print(dictionar)
for key in dictionar:
    print(key, dictionar[key])


# Dictionary comprehensions
# values = {}
# for x in range(5):
#     values[x] = x * 2

# values = {x: x * 2 for x in range(5)}
# print(values)

# Generator Expressions
values = (x * 2 for x in range(1000))
print(getsizeof(values))

# Unpacking operator
numb = [1, 2, 3]
print(*numb)
print(1, 2, 3)

result = list(range(5))
result = [*range(5), *"Hello"]
# print(result)

first = {"x": 1}
second = {"x": 10, "y": 22}
combined = {**first, **second, "z": 1}
print(combined)

# Character frequency
sentence = "This is a common interview question"
char_freq = {}
for char in sentence:
    if char == " ":
        continue
    char_freq[char] = char_freq.get(char, 0) + 1

# Sort by frequency to see winner
sorted_freq = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)
print(sorted_freq[0])
