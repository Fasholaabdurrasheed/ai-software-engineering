# Lesson 3 part 2 challenge

# Create a tuple
coordinates = (6.5244, 3.3792)

# print both values
print(coordinates)

# print the length
print(len(coordinates))

# try changing the first value
# coordinates[0] = 7.0

# Challenge 2 - Set
numbers = {1, 2, 3, 3, 4, 4, 5}

# print the set
print(numbers)

# print its length
print(len(numbers))

# add 6
numbers.add(6)
numbers.add(3)
# it is stated in the method that This has no effect if the element is already present and 3 is present already is it has no effect
print(numbers)

# check whether 4 exists.
if 4 in numbers:
    print("4 is Present")

# check whether 10 exists
if 10 in numbers:
    print(f"{10} is present in the set ")
else:
    print(f"{10} is not present in the set")

# Challenge 3 - Real-world set
skills = [
    "Python",
    "SQL",
    "Python",
    "R",
    "SQL",
    "Machine Learning", 
    "Python"
]
print(skills)

# convert the list to a set
skills_to_set = set(skills)
print(skills_to_set)