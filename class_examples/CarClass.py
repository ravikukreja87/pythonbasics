class Car:
    """A class to represent a Car ; Model of a car"""
    def __init__(self, make, model, year, type_of_car):
        self.make = make
        self.model = model
        self.year = year
        self.type_of_car = type_of_car
        self.number_of_wheels = 4       #Default value to he number of wheels attr
        self.odometer_reading = 0
        self.fuel_tank_capacity = 45

    def get_car_details(self):
        print(f"This is {self.make} {self.model} car, manufactured in {self.year} and uses {self.type_of_car}, has {self.number_of_wheels} wheels and initial odometer reading is {self.odometer_reading}")

    def drive(self, km):
        print(f"{self.make} is driving for {km} kms")
        audi.odometer_reading = audi.odometer_reading + km

    def get_odometer_reading(self):
        print(f"Current odometer reading of {self.make} is {self.odometer_reading}")

    def fill_fuel(self):
        print(f'Filling fuel in {self.model} car upto {self.fuel_tank_capacity} ltrs.')


audi=Car("Audi", "A5",2020, "Petrol")
bmw=Car("BMW", "E Series",2023, "Electricity")
# audi.get_car_details()
# audi.get_odometer_reading()
# audi.drive(10) #Session1
# audi.drive(20)  #Session2
# audi.get_odometer_reading()
# # audi.show_battery_details()
# bmw.get_odometer_reading()
# bmw.fill_fuel()