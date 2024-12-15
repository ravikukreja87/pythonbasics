with open(
        'C:/Training2023/2024/PythonProjects/MyFirstPythonProject/MyFirstPythonProject/files/sample.txt') as file_object:
    for line in file_object:
        if 'Tom' not in line:
            print(line.rstrip())
