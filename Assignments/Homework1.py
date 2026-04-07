from matplotlib import pyplot
import numpy
from mpl_toolkits.mplot3d import Axes3D

# data for each country
country_names = ["Austria", "Italy", "Netherlands", "Switzerland", "Turkey"]
r_list = [0.195, 0.099, 0.114, 0.163, 0.144]
N_list = [14700, 216600, 42580, 28400, 133700]

# initial number of infected people
P0 = 100
days = 31
day_values = numpy.arange(0, days + 1, 1)

#value computation
print("INFECTED PEOPLE FOR 31 DAYS")
print()

for c in range(len(country_names)):
    print(country_names[c])
    
    r = r_list[c]
    N = N_list[c]
    
    P_values = [P0]
    
    for i in range(days):
        Pi = P_values[i]
        next_value = Pi + r * Pi * (1 - Pi / N)
        P_values.append(next_value)
    
    for i in range(days + 1):
        print(f"Day {i}: {P_values[i]:.2f}")
    
    print()

# 2D graph
selected_country = "Turkey" #choose country for 2D graph
selected_r = 0
selected_N = 0

for c in range(len(country_names)):
    if country_names[c] == selected_country:
        selected_r = r_list[c]
        selected_N = N_list[c]

P_values = [P0]

for i in range(days):
    Pi = P_values[i]
    next_value = Pi + selected_r * Pi * (1 - Pi / selected_N)
    P_values.append(next_value)

pyplot.plot(day_values, P_values)
pyplot.xlabel("Day")
pyplot.ylabel("Infected People")
pyplot.title("2D Graph for " + selected_country)
pyplot.grid()
pyplot.show()

# 3D graph

r_surface = numpy.linspace(min(r_list), max(r_list), 30)

# make x and y grids
X, Y = numpy.meshgrid(day_values, r_surface)

# make z grid
Z = numpy.zeros((len(r_surface), len(day_values)))

N = selected_N #keeps N fixed

for row in range(len(r_surface)):
    r = r_surface[row]
    P = P0
    Z[row][0] = P
    
    for col in range(1, len(day_values)):
        P = P + r * P * (1 - P / N)
        Z[row][col] = P

ax = pyplot.axes(projection='3d')
ax.plot_surface(X, Y, Z)

ax.set_xlabel("Day")
ax.set_ylabel("Growth Rate (r)")
ax.set_zlabel("Infected People")

pyplot.title("3D Surface Graph")
pyplot.show()