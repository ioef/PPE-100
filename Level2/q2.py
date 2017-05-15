#!/usr/bin/env python
'''
Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.
'''

x=10
y=5

#create the array with the above dimensions
#for every row create a number of columns
array = [[0 for col in range(y)] for row in range(x)]


#fill the array 
for row in range(0, x):
    for col in range(0, y):
        array[row][col] = row*col


print array
