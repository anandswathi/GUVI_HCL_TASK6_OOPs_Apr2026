"""
Python Task-6

Problem 3: Vehicle Rental

Create a base class Vehicle with attributes like model, rental_rate, and a method calculate_rental().
Inherit from this class to create subclasses Car, Bike, and Truck. Each subclass should have specific
attributes and calculations for rental rates.

Implement polymorphism to calculate the rental cost of different vehicles based on their type and
rental duration.
"""

# Base Class Vehicle
class Vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental(self, days):
        pass

# Class Car inheriting from base class Vehicle
class Car(Vehicle):
    def __init__(self, model, rental_rate, car_type):
        super().__init__(model, rental_rate)
        self.car_type = car_type

    def calculate_rental(self, days):
        return self.rental_rate * days

# Class Bike inheriting from base class Vehicle
class Bike(Vehicle):
    def __init__(self, model, rental_rate, deposit):
        super().__init__(model, rental_rate)
        self.deposit = deposit

    def calculate_rental(self, days):

        # Deposit calculation - 20 percentage of rental amount
        deposit = (self.rental_rate * days) * 0.2
        return (self.rental_rate * days) + deposit

# Class Truck inheriting from base class Vehicle
class Truck(Vehicle):
    def __init__(self, model, rental_rate, load_capacity, load_type, total_distance):
        super().__init__(model, rental_rate)
        self.load_capacity = load_capacity # Calculated in tons
        self.load_type = load_type # Small/Medium/Heavy type
        self.total_distance = total_distance # Total distance covered in kms

    def calculate_rental(self, days):
        base_fare = self.rental_rate * days # Basic fare
        extra_charge = 0 # Extra charge based on loads

        if self.load_type == "small": # For Mini Trucks/Tempos

            # Extra charge based on total distance covered in kms
            extra_charge = self.total_distance * self.rental_rate

        elif self.load_type == "medium": # For Medium Commercial Vehicles

            # Extra charge based on load capacity in tons
            extra_charge = self.load_capacity * 25

        elif self.load_type == "heavy": # For Heavy Commercial vehicles

            # Extra charge based on load capacity in tons
            extra_charge = self.load_capacity * 55

        return (self.rental_rate * days) + extra_charge

# Demonstrating polymorphism
car = Car("MS Swift Desire", 350, "sedan")
bike = Bike("TVS Victor", 200, 100)
truck = Truck("Ashok Leyland BOSS ", 800, 10, "heavy", 3000)

vehicleType_vehicle_obj_dict = {"CAR": car, "BIKE": bike, "TRUCK": truck}

days = int(input("No. of days: ")) # Get the no. of days for the rental to be calculated from user

for vehicle, veh_obj in vehicleType_vehicle_obj_dict.items():
    print("{} ---> {} Rental Cost for {} days: Rs.{}".format(vehicle, veh_obj.model, days, veh_obj.calculate_rental(days)))









