#2.    Write a class named MyDate designed to store information about a date. Define a constructor in the MyDate class that takes date components as arguments and attaches them to the object. Additionally, define a corresponding method in the MyDate class that interprets a MyDate object as a string.

class MyDate():
    def __init__(self, month, day, year):
        self.year = year
        self.month = month
        self.day = day
    
    def __str__(self):
        return f"{self.month:02}/{self.day:02}/{self.year}"

md = MyDate(3,23,1985)

print(md)