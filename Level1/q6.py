#!/usr/bin/env python
'''
Write a method which can calculate the area of a circle
Hints: Using the ** Operator
'''

pi=3.14

def circleArea(radius):
    area = pi * radius * radius
    return area 

#radius = 2cm
print("The area of a circe with {0} radius is {1}cm".format("2cm",circleArea(2)))

