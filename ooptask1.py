# OOP TASK 1.Create a Car Class Have the following attributes

# brand - model - year -fuel_capcity - fuel_level -is_running(boolen value) Have the methods
# start()
# stop()
# refuel()
# drive()
# display_car_info()

class Car:
    def __init__(self, brand, model, year, fuel_capacity):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_capacity = fuel_capacity
        self.fuel_level = 0  # starts empty
        self.is_running = False #Engine is off at the beginning

    def start(self):
        if self.fuel_level > 0:
            self.is_running = True
            print(f"{self.brand} {self.model} has started.")
        else:
            print("Car cannot start since Fuel tank is empty!")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.brand} {self.model} stopped.")
        else:
            print("Car is already stopped.")

    def refuel(self, amount):
        if amount <= 0:
            print("Refuel amount must be positive.")
            return
        if self.fuel_level + amount > self.fuel_capacity:
            self.fuel_level = self.fuel_capacity
            print("Tank is full now.")
        else:
            self.fuel_level += amount
            print(f"Added {amount} liters. Current fuel: {self.fuel_level} liters.")

    def drive(self, distance):
        if not self.is_running:
            print("Start the car first!")
            return
        fuel_needed = distance * 0.1  # assume 1 liter per 10km
        if fuel_needed > self.fuel_level:
            print("Not enough fuel to drive that distance.")
        else:
            self.fuel_level -= fuel_needed
            print(f"Drove {distance} km. Remaining fuel: {self.fuel_level:.2f} liters.")

    def display_car_info(self):
        print("Car Information:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Fuel Capacity: {self.fuel_capacity} liters")
        print(f"Fuel Level: {self.fuel_level} liters")
        print(f"Is Running: {self.is_running}")


car1 = Car("Subaru", "Forester", 2019, 63)
car2 = Car("Mazda", "CX5", 2020, 67)

car1.refuel(20)
car2.refuel(45)

car1.drive(100)

car1.display_car_info()
# car2.display_car_info()

       