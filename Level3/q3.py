#!/usr/bin/env python
'''
Level 3

Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield
'''

class dividercheck():
   def  __init__(self,  number):
       self.number = number

   def numbers(self):
       for num in range(0,self.number+1):
           if num%7 ==0:
               yield num

      

num = int(raw_input("Please give a number:"))

a = dividercheck(num)

for i in a.numbers():
    print i
