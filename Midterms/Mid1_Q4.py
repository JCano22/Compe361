#4.    Create a class called `Movable` designed to store information about an object capable of moving. The class should include a field named `Speed`. Next, create another class called `Engine` designed to store information about an object with a motor. This class should include a field named `Force`. Then, create a class called `Vehicle`, which is intended to store information about a movable object with a motor. This class should inherit from both the `Movable` and `Engine` classes. Define a method called `Print` in the `Vehicle` class that prints the values of all its fields. Each class should have a constructor that takes parameters and assigns them to the respective fields.

class Movable:
    def __init__(self, speed):
        self.speed = speed

class Engine:
    def __init__(self, force):
        self.force = force

class Vehicle(Movable, Engine):
    def __init__(self, speed, force):
        Movable.__init__(self, speed)
        Engine.__init__(self, force)
        
    def print(self):
        print(self.speed)
        print(self.force)

v = Vehicle(50, 100)
v.print()
