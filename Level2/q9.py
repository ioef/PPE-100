#!/usr/bin/env python
'''
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

num = raw_input("Give a number:")

#the followin are of string type. Therefore we apply string calculations-concatenation operations
num1= num
num2= num*2
num3= num*3
num4= num*4

total = int(num1) + int(num2)  + int(num3) + int(num4)

print total
