#!/usr/bin/env python
'''
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

numlist =[]
for i in range(1000,3001):
    i_str = str(i)
  
    if (int(i_str[0])%2==0) and (int(i_str[1])%2==0) and (int(i_str[2])%2==0):
        numlist.append(i_str)

print ' '.join(numlist)
