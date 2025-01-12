from faker import Faker

fake_object = Faker('en_US')

for i in range(500):
    print(f'Record Number - {i+1}')
    print(fake_object.unique.name())
    print(fake_object.address())
    print("==========================")