from class_examples.Battery import Battery
from class_examples.CarClass import Car



class ElectricCar(Car):
    """ElectricCar is child class of class Car"""

    def __init__(self, make, model, year, type_of_car):
        super().__init__(make, model, year, type_of_car)
        self.battery = Battery(150)  #Object/Instance of battery class

    def fill_fuel(self): #Overriden function/method
        print(f'This is electric car, fuel filling is NA')

make_tata='Tata'
nexon = ElectricCar(make_tata, 'Nexon', 2022, 'Electricity')
nexon.get_car_details()
nexon.battery.show_battery_details(make_tata)
nexon.battery.range()
nexon.fill_fuel()
# Since fill fuel is not applicable for this class, so we can override the method
make_mg='MG'
mg = ElectricCar(make_mg,'Hector',2023,'Electricity')
mg.battery = Battery(200)
mg.battery.show_battery_details(make_mg)
mg.battery.range()
# Parent class CANNOT use functions/attrs of child class