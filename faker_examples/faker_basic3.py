from faker import Faker

fake_object = Faker()
phone = fake_object.phone_number()



print(phone)
