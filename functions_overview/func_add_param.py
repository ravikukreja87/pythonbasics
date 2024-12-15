# Number of arguments/parameters in function add are not fixed
def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)
    return sum
#numbers will be treated as tuple here by python

add(2, 3)
add(4, 5, 6)
add(1, 5, 6, 7, 8, 9, 0, 1)
