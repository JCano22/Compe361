#3.    Create a `Country` class intended to store information about a country model. In the class, define a constructor that attaches the following fields to the class object: `name`, `population`, and `area`. Also, define a method called `density` that calculates the population density for the country (calculated as the population of the country divided by the area of the country). Finally, provide an example of creating an object of this class and invoking its methods.

class Country:
    def __init__(self, n, p, a):
        self.name = n
        self.population = p
        self.area = a
    
    def density(self):
        if self.area == 0:
            raise Exception("Area can't be 0 when calculating density.")
        return self.population / self.area
    
c = Country("SD", 1000000, 2000000)
print(c.density())