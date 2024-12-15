import json

numbers = [2, 4, 6, 8, 0]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
