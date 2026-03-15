# 5.    Create a class called `Triangle` designed to store the lengths of the three sides of a triangle. Define a method named `Perimeter` within the `Triangle` class, which returns the sum of the lengths of all three sides. Next, create a class called `Pentagon` that inherits from the `Triangle` class and is intended to store the lengths of five sides of a pentagon. The `Pentagon` class should have two additional fields for the two extra sides, as the other three sides can be stored in the fields inherited from the `Triangle` class. Override the `Perimeter` method in the `Pentagon` class so that it returns the sum of the lengths of all five sides of the pentagon.

class Triangle:
    a = 1
    b = 2
    c = 3
    def perimeter(self):
        return self.a + self.b + self.c

class Pentagon(Triangle):
    d = 4
    e = 5
    def perimeter(self):
        return super().perimeter() + self.d + self.e
    
u = Pentagon()
p = u.perimeter()

print(p)