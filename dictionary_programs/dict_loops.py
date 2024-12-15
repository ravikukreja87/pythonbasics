# Basic loop

student_database = {1: 'Jon', 2: 'Mark', 3: 'Tom'}

for key, value in student_database.items():
    if value == 'Mark':
        student_database[key] = 'Greg'
        print(f'Name {value} is replaced with Greg')

for key, value in student_database.items():
    print(f'Roll Number : {key}')
    print(f'Name : {value}')
    print('-------------------')

print(student_database)
# Replace Mark with Greg
