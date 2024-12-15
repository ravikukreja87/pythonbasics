from io import UnsupportedOperation

with open('../files/sample.txt') as file_object:
    data = file_object.read()
    try:
        file_object.write('Test')
    except UnsupportedOperation:
        print('Cannot write. Make sure to open file for writing')

    #data variable contains all the data that is present in the file
print(data)