
# Scenario: Vehicle, Car, Bike
# Create a Vehicle class with a method fuel_capacity().
# Then, create two subclasses: Car and Bike, both of which inherit from Vehicle. Each should override the fuel_capacity() method to give different values for cars and bikes.
# Demonstrate how both Car and Bike objects can call their own fuel_capacity() method.

# Tasks:
# Implement the Vehicle class with the fuel_capacity() method.
# Implement the Car class inheriting from Vehicle and overriding the fuel_capacity() method.
# Implement the Bike class inheriting from Vehicle and overriding the fuel_capacity() method.
# Create instances of Car and Bike and test the overridden fuel_capacity() methods.

class Vehicle:
    def fuelCapacity(self):
        return self

class Car(Vehicle):
    def fuelCapacity(self):
        return "Car Fuel Capacity : 50L"
    
    
class Bike(Vehicle):
    def fuelCapacity(self):
        return " Bike Fuel Capacity : 20L"


car=Car()
bike=Bike()
print(car.fuelCapacity())
print(bike.fuelCapacity())   
    