'''Calculate volume of a sphere by prompting user for radius.'''


#importing pi value from math module and using alias we name as pi_value
from math import pi as pi_value
radius_of_the_sphere = int(input())
#Now calculating the volume of the volume of the sphere using the formulae
Volume_of_the_sphere = round((4/3)*pi_value*((radius_of_the_sphere)**3),2)
print(Volume_of_the_sphere)