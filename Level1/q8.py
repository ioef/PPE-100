#!/usr/bin/env python
'''
Define a class, which have a class parameter and have a same instance parameter.

Hints: Define a instance parameter, need add it in __init__ method
    You can init a object with construct parameter or set the value later
'''

class Human():
     #the name is the class parameter
     name = "Person"
     
     def __init__(self,name=None):
         #self.name is the instance parameter
         self.name = name
         self.age  = 0

#instanstiation and setting of the name for the class Human
human1 = Human("Lex Luthor")
print ("{0} name is {1}".format(Human.name, human1.name))

human2 = Human()
human2.name = "Dr. Doom"
print ("{0} name is {1}".format(Human.name, human2.name))
