
# Scenario 3: Multilevel Inheritance >>>>>>>

# Scenario: Animal, Mammal, Dog
# Create an Animal class that has a method eat().
# Then, create a Mammal class that inherits from Animal and has an additional method walk().
# Finally, create a Dog class that inherits from Mammal and has a method bark().
# Demonstrate how a Dog object can use methods from all three classes.

# Tasks:
# Implement the Animal class with the eat() method.
# Implement the Mammal class that inherits from Animal and adds the walk() method.
# Implement the Dog class that inherits from Mammal and adds the bark() method.
# Create an instance of Dog and call the eat(), walk(), and bark() methods.

class Animal:
    def eat(self):
        return "eating"

class Mammal(Animal):
    def walk(self):
        return "walking"

class Dog(Mammal):
    def bark(self):
        return "barking" 


dog=Dog()


print(dog.eat())
print(dog.bark())
print(dog.walk())