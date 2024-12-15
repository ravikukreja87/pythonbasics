import json

username = input("Enter Student Name: ")

filename = "student_name.json"

data = f'\n{username}'

with open(filename, 'a') as f:
    # json.dump(username, f)
    json.dump(data, f)
    print(f'{username} is saved in {filename}')
