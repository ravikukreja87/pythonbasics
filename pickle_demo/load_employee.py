import pickle

with open('employee.dump','rb') as file:
    employees = pickle.load(file)

print(employees)