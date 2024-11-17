# Odd even identifier generator

for num in range(1, 20):
    if num % 2 == 0:
        print(f"Even Number {num}")
        continue        #Skipping rest of the lines in loop code and going to line 4 again with next iteration
    print(f"Odd Number {num}")

print("End of program")
