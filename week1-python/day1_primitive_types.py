# week1-python/day1_primitive_types.py
# Aleksei Ivanov – QA Automation Portfolio – Week 1
# Pure Python basics

# Variables
students_count = 1000
rating = 4.99
is_published = False
course_name = "Python Programming"

print(students_count, rating, is_published, course_name)
print(len(course_name))
print(course_name[0])
print(course_name[0:3])

# Strings
course = 'Programming "Python"\nnew line   '
print(course)

first = "Aleksei"
last = "Ivanov"
full = first + " " + last
full_name = f"{first} {last}"
print(full, full_name)

# String methods
print(course.upper())
print(course.title())
print(course.strip())
print(course.find("Py"))
print(course.replace("Pro", "Rpo"))
print("Pro" in course)
print("Tag" not in course)
