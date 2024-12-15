def add(first_number, second_number):
    sum = first_number + second_number
    print(f'Addition\n{first_number} + {second_number} = {sum}\n---------')
    return sum  # value of variable sum is returned wherever the function sum is called


add(add(3, 5), add(7, 10))

sum_var = add(4, 6)
# print(f'sum_var {sum_var}')
# add(4, 60)
# add(4, 600)

# Return values

# Problem Statement is --> Add 3+5 and Add 7+10 and then add result of both of these sums
# (3+5) + (7+10) --> print this
# total = add(3, 5) + add(7, 10)
# print(f'Total : {total}')
