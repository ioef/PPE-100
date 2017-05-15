#!/usr/bin/env python
'''
Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.
 
Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
'''

def printList():
    numlist=[]
    for i in range(1,21):
         numlist.append(i*i)

    return numlist[-5:]


print(printList())
