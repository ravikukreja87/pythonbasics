class Battery:
    """This class models Batteries of Car"""

    def __init__(self, battery_capacity=110):
        self.battery_capacity = battery_capacity

    def show_battery_details(self, make):
        print(f'{make} car has a battery of {self.battery_capacity}-kWH')

    def range(self):
        """Informs how much kms can be covered with a given battery capacity"""
        #3 kms can be covered for every kWH of batter
        total_range = 3.5 * self.battery_capacity
        print(f'Total Range that can be covered with this battery of {self.battery_capacity}-kWH is {total_range} kms')