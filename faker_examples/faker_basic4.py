from faker import Faker

fake_object = Faker()
date = fake_object.date_time()



print(date)
