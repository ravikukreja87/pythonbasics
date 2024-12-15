# Print largest number
# 10 , 20 , 30
# Z is the largest and X is smaller than Y
# Z is the largest and X is not smaller than Y

X = 21
Y = 200
Z = 30

if Z > X and Z > Y:         #Outer If Block (Level 0)
    print('Z is largest')
    # If flow is here, it proves that Z is largest
    if X < Y:               #Inner if block 1 (Level 1)
        print('Z is the largest and X is smaller than Y')
    else:               #Inner else block 1
        print('Z is the largest and X is not smaller than Y')
else:                       #Outer else block
    if Y > X:       #Inner if block 2 (Level 1)
        print('Y is largest')
        # If flow is here, it proves that Y is largest
        if X < Z:       #Inner if block 3   (Level 2)
            print('Y is the largest and X is smaller than Z')
        else:           #Inner else block 3
            print('Y is the largest and X is not smaller than Z')
    else:       #Inner else block 2
        print('X is largest')
        # If flow is here, it proves that X is largest
        if Y < Z:           #Inner if block 4 (Level 2)
            print('X is the largest and Y is smaller than Z')
        else:               #Inner else block 4
            print('X is the largest and Y is not smaller than Z')
