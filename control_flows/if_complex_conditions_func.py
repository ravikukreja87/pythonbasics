# Print largest number
# 10 , 20 , 30
# Z is the largest and X is smaller than Y
# Z is the largest and X is not smaller than Y

X = 3100
Y = 200
Z = 300


def compare(first, alias_first, second, alias_second, largest):
    if first < second:  # Inner if block 1 (Level 0)
        print(f'{largest} is the largest and {alias_first} is smaller than {alias_second}')
    else:  # Inner else block 1
        print(f'{largest} is the largest and {alias_first} is not smaller than {alias_second}')


if Z > X and Z > Y:  # Outer If Block (Level 0)
    print('Z is largest')
    # If flow is here, it proves that Z is largest
    compare(X, 'X', Y, 'Y', 'Z')
else:  # Outer else block
    if Y > X:  # Inner if block 2 (Level 1)
        print('Y is largest')
        # If flow is here, it proves that Y is largest
        compare(Z, 'Z', X, 'X', 'Y')
    else:  # Inner else block 2
        print('X is largest')
        # If flow is here, it proves that X is largest
        compare(Y, 'Y', Z, 'Z', 'X')
