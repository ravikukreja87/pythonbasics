def add_student_detail(**student_info):
    print(student_info['name'])
    print(student_info['section'])


add_student_detail(name='jon', section='B', age=10, grade=5)  # name, age, grade
add_student_detail(name='mark', section='A', grade=5)  # name, age, grade
