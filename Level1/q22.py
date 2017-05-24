#!/usr/bin/env python
'''
Create a function that accepts a number and return it's absolute value
'''

def abs(number):
    if number >=0:
        return number
    else:
        return -number


print(abs(-5))
print(abs(0))
print(abs(100))

