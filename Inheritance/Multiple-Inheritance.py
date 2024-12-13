#  Scenario: Writer and Painter
# A person can be both a Writer and a Painter.
# Create a Writer class that has a write() method and a Painter class that has a paint() method.
# Now, create a CreativePerson class that inherits from both Writer and Painter and can use both the write() and paint() methods.

# Tasks:
# Implement the Writer class with a write() method.
# Implement the Painter class with a paint() method.
# Implement the CreativePerson class inheriting from both Writer and Painter.
# Create an instance of CreativePerson and demonstrate calling both write() and paint() methods.

class Writer:
    def write(self):
        return "Writing a book."
    
class Painter:
    def paint(self):
        return "painting a canvas."

class creativePerson(Writer,Painter):
    pass


creative_Person=creativePerson()
print(f"Creative Person:\n{creative_Person.write()}\n{creative_Person.paint()}")