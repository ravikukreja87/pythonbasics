# Print first 10 multiples of 5
# 0, 5, 10, 15
from turtledemo.penrose import start

start=int(input("Enter start : "))
end=int(input("Enter end : "))
num=int(input(f"Enter number to find its multiples between {start} and {end} : "))
listOfMultiples=list(range(start,end,num))
print(f"List of multiples of {num} is {listOfMultiples}")


# for i in range(0,51,6):
#     print(i)

    #Iteration 1 - The value of i will be 0
    #Iteration 2 - The value of i will be 5
    # Iterations will keep on going till i becomes 50