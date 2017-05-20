#!/usr/bin/env python
'''
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

values=[]

numbers = [ x for x in raw_input('Give 4digits binary number with comma e.g. 1001,0001 :').split(',')]


for num in numbers:
    #convert to integer and check if is divisable by 5
    if int(num,2) % 5 == 0:
         values.append(num)

print ' '.join(values)
