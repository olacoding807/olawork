# Global variable
company_name = "AutoWorld"

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        # Accessing global variable
        print(f"Company: {company_name}, Car Brand: {self.brand}, Model: {self.model}")

# Subclass inheriting from Car
class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)  # Calling the constructor of the parent class
        self.battery_capacity = battery_capacity
    
    def display_info(self):
        super().display_info()  # Calling the parent class method
        print(f"Battery Capacity: {self.battery_capacity} kWh")

# Subclass for Petrol Cars
class PetrolCar(Car):
    def __init__(self, brand, model, power):
        super().__init__(brand, model)  # Calling the constructor of the parent class
        self.power = power  # Corrected the variable assignment
    
    def display_info(self):
        super().display_info()  # Calling the parent class method
        print(f"Engine Power: {self.power} cc")  # Fixed the display text

# Creating objects
car1 = Car("Ford", "Mustang")
ecar1 = ElectricCar("Tesla", "Model S", 100)
pcar = PetrolCar("Ferrari", "Spyder", 233)

# Calling methods
car1.display_info()
print()
ecar1.display_info()
print()
pcar.display_info()
