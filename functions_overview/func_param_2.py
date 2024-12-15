# Functions can be used to pass the data as well

def hello_world(user, grade=0):
    print(f'Hello World! Welcome {user} to grade {grade}')


hello_world('Tom', 5)
hello_world('Jon', 7)
hello_world('Mark', 9)

# Order of the arguments/parameters must be correct
hello_world(10, 'Greg')

# Pass parameters with argument name
hello_world(grade=10, user='Henry')

# Default values
hello_world(user='Steve')
