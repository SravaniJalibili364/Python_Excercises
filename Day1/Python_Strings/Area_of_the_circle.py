'''Calculate area of a circle by prompting user for radius.'''

#importing pi from math module
from math import pi as pi_value

radius_input = int(input())
# Calculating the area of the circle by using the formula (pi)*r**2 formulae
area_of_the_circle = round(pi_value*(radius_input**2),2)
print(area_of_the_circle)