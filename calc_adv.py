choice='n'
while choice != 'y':        # n not equal to y --> true #if user enters choice = y , y!=y --> False
    numberOne = int(input("Enter first number : "))
    operator = input("Enter operation you want to perform (+,-,*,/) : ")
    numberTwo = int(input("Enter second number : "))


    if operator == '+':
        print(f"Addition of two numbers is : {numberTwo + numberOne}")
    if operator == '-':
        print(f"Subtraction of two numbers is : {numberOne - numberTwo}")
    if operator == '*':
        print(f"Multiplication of two numbers is : {numberTwo * numberOne}")
    if operator == '/':
        divisionResult = round(numberOne / numberTwo,1)
        print(f"Division of two numbers is : {divisionResult}")
    choice = input("Do you want to close the calculator (y/n) : ") #user can enter y/n
    # if choice is y then close else continue to ask First Number
    # we have to run calc continuously till user chooses y

print("Exiting")

# **
# %
# //