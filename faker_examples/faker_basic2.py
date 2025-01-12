from faker import Faker

fake_object = Faker()
address = fake_object.address()

another_address = str(fake_object.random_int(100,10000)) + "/" + fake_object.street_address() + "\n" + fake_object.city() + " " + str(fake_object.random_int(100000,999999))

print(another_address)
