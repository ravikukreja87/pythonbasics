colors = ['Green', 'Red', 'Blue']
colors = colors + ['Black']

# Whatever data is there in colors list, put that data one by one in eachColor variable
# Python interpreter detects size of list automatically and iterates over the code for number of times = size of list
for eachColor in colors:
    print(f"Current Color is {eachColor} and number of characters are {len(eachColor)}")
