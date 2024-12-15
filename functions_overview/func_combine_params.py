# Number of arguments/parameters in function add are not fixed
def add(base, *numbers):
    print(base)
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)

    return sum


# numbers will be treated as tuple here by python

add("Add", 3, 1)
add("Add", 5, 6)
add("Add", 5, 6, 7, 8, 9, 0, 1)
