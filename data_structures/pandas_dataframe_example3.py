import pandas

students = [
    [1, "Jon"],
    [2, "Mark"],
    [3, "Tom"]

]

indexes = ['row 1','row 2','row 3']


students_s = pandas.DataFrame(students, columns=['Roll Number','Name'], index=indexes)

print(students_s)
