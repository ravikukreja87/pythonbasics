import os
import csv

print(os.path.dirname(os.path.realpath(__file__)))
#Above stmt provides location of my current script/file
# C:\Training2023\2024\PythonProjects\MyFirstPythonProject\MyFirstPythonProject\data_driven

csv_file = os.path.dirname(os.path.realpath(__file__)) + "/sample.csv"
f = open(csv_file, 'rt')

reader = csv.reader(f)
for row in reader:
    # print(row)
    user_name = row[0]
    user_password = row[1]
    print(user_name)
    print(user_password)

f.close()
