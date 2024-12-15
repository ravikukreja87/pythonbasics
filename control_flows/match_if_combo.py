# Combine Match and If
# List of numbers
# We need to identify if a number is +ve, -ve or 0

numbers = [5, 3, -1, 0, -6, 8]

for number in numbers:          #number=5
    match number:
        case n if n > 0:            #n=number or n=5
            print(f'{n} is positive')
        case n if n < 0:            #n=-1
            print(f'{n} is negative')
        case 0: #n is not present here . We dont need to assign number to n
            print('Zero')
        case _:
            print('Unknown')
