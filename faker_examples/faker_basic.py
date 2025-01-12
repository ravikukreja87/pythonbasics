from faker import Faker

fake_object = Faker()
emp_name = fake_object.first_name() + " " + fake_object.last_name() + " knows " + fake_object.language_name() + " language."

print(emp_name)
