#2.    Write a class named MyDate designed to store information about a date. Define a constructor in the MyDate class that takes date components as arguments and attaches them to the object. Additionally, define a corresponding method in the MyDate class that interprets a MyDate object as a string.

class MyDate:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    def __str__(self):
        return (str(f"{self.month:02}/{self.day:02}/{self.year}"))

today = MyDate(5,5,2026)

print(today)