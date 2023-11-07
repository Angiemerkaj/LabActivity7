#!bin/usr/bin/env
#Enxhi Merkaj 11/07/2023

import math

#Function that calculates area of circle

def areaOfCircle(r):
    if r < 0:
        return "Radius cannot be negative"
    else:
        area = math.pi * (r ** 2)
        return area

r = float(input("Enter the radius of the circle: "))

print("%f" %areaOfCircle(r))
