# Dictionary - This data type in python stores key-value pairs

# For student roll number and name example
#   Roll number is a key with data type as number
#   Name is a value with data type as string
#   key:value
student_database = {1: 'Jon', 2: 'Mark', 3: 'Tom'}  # key is number data type and value is string data type

# In Telephone dictionary - Name is key and phone number is value
# In Telephone dictionary - Name is String data type and phone number is number data type

telephone_directory = {"Jon": 711, "Mark": 722, "Tom": 733,
                       "Jon": 744}  # key is string data type and value is number data type

email_database = {'Jon': 'jon@test.in', 'Mark': 'mark@test.in',
                  'Tom': 'tom@test.in'}  # Key and value both are String data type

# print(student_database[1])
# print(telephone_directory['Jon'])










car = {'color': 'white', 'top_speed': 100}  # Mixed data types in value
# print(car['color'])
print(car)

car['type'] = 'sedan'
car['engine_capacity'] = 1500
print(car)
#Order of insertion is maintained in dictionary

#We can initialize empty dictionary as well
student={}
print(student)
student['name']='Greg'
print(student)
student['name']='Tom'   #Edit/update the items already present in dictionary
print(student)

# Loop through all the name values --> Find the name that we want under if statement and replace it

#Removing items from dictionary
del car['top_speed']
print(car)

#Normally we use dictionary for similar kind of objects