#!/usr/bin/env python
'''
Define a class named American which has a static method called printNationality.

Hints:
Use @staticmethod decorator to define class static method.
'''

class American:
    @staticmethod
    def printNationality():
        print "America"


American.printNationality()

anAmerican = American()
anAmerican.printNationality()



