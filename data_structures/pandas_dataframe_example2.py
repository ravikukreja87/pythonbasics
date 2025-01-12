import pandas

animals = {
    'animal_type': ['dogs', 'cats', 'rats', 'camels'],
    'name': ['A', 'B', 'C', 'D'],
    'age': [2, 3, 45, 5],
    'city': ['C', 'I', 'T', 'Y']
}

indexes = ['a', 'b', 'c', 3]

animals_s = pandas.DataFrame(animals, indexes)

print(animals_s)
