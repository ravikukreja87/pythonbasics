# Dictionary of employees
import pickle

employees = [
    {'name': 'Jon', 'id': 7},
    {'name': 'Mark', 'id': 14},
    {'name': 'Tom', 'id': 21}
]

print(employees)

# Serializa this dictionary
with open('employee.dump', 'wb') as file:
    pickle.dump(employees, file)
#Dictionary object will be serialized (saved) in employee.dump file
serialized_data = pickle.dumps(employees)
print(serialized_data)