#!/usr/bin/env python
'''
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
0If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

from  math import *

pos = [0,0]

while True:
    data = raw_input("Give direction and number of steps e.g UP 5:")
 
    if data:
        movement = data.split(' ')
        direction = movement[0].upper()
        steps     = int(movement[1])

        if direction =='UP':
            pos[0]+=steps
        elif direction == 'DOWN':
            pos[0]+=steps
        elif direction == 'RIGHT':
            pos[1]+=steps
        elif direction == 'LEFT':
            pos[1]-=steps
        else:
            pass
    else:
        break

distance = int(sqrt(pos[0]**2 + pos[1]**2))

print "The distance from the zero point is {0}".format(distance)
