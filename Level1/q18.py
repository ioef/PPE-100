#!/usr/bin/env python
'''
Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

Hints:
Use unicode() function to convert.
'''

s = raw_input("Give text:")

u = unicode(s, "utf-8")

print u
