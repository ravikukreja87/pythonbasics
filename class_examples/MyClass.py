class Dog:
    """A sample.txt dog class which represents and models a dog"""

    def __init__(self, name, age, height, weight):
        """Initialize the properties of the object/instance that we will created when invoking the object"""
        # We will write  code to initialize these attributes here
        # Attributes the classes/objects
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def sit(self):
        print(f"{self.name} is now sitting")

    def eat(self):
        print(f"{self.name} is eating")

    def digest(self):
        print(f"{self.name} is digesting")


first_dog = Dog("Bruno",4,2.5,5)
second_dog = Dog("Tommy",4,3,4)

print(f"First dog's name is {first_dog.name} with age {first_dog.age}")
first_dog.sit()
first_dog.eat()
print(f"Second dog's name is {second_dog.name}")
second_dog.digest()