from random import choice

numbers = [2, 4, 6, 7, 1, 3]
students = ['Jon','Mark','Tom']

random_number = choice(students)
print(random_number)

#Class Names must be in CamelCase or InitCaps
# RandomExample Correct
# Randomexample Incorrect randomexample random_example
#Instance and module names should be all lower case with underscore between words