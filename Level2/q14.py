#!/usr/bin/env python
'''
Question:
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 

Hints:

Use if statement to judge condition.
'''

text = raw_input("Give a text input:")

if text =="yes" or text =="YES" or text =="yes":
    print "Yes"
else:
   print "No"
