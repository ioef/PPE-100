#!/usr/bin/env python

'''
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters
'''

class StringHandler():
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = raw_input("Enter a string:")

    def printString(self):
        print (self.text.upper())


sHandler = StringHandler()
sHandler.getString()
sHandler.printString()
