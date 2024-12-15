divisionResult=0
numberOne = 20
numberTwo = 0

try:
    # divisionResult = 0
    print(f"Addition of two numbers is : {numberTwo + numberOne}")
    print(f"Subtraction of two numbers is : {numberOne - numberTwo}")
    divisionResult = round(numberOne / numberTwo, 1)  # ZeroDivisionError
except ZeroDivisionError:
    pass
    # print('Cannot divide by zero')

print(f"Division of two numbers is : {divisionResult}")
print(f"Multiplication of two numbers is : {numberTwo * numberOne}")


# Cannot divide by zero

# Goal :- Handle such exception scenarios gracefully. (This is not invalid because 0 is a valid input)

# 1. Identify lines of code where there is probability of exception -  0%-100%
# 2. Surround identified lines of code under try: block
# 3. What to do if I get exception or What to do if I don't get an exception
