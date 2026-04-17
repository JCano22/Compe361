#Write a Python application which will construct this plot using matplotlib library.

import matplotlib.pyplot as pyplot

x = (3, 5, 8, 11, 13, 17, 19)
y = (50, 35, 45, 25, 35, 20, 25)

pyplot.plot(x, y)
pyplot.show()