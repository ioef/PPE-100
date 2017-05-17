#!/usr/bin/env python
'''
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''

sentence = raw_input("Give a sentence:")

letters=0
numbers=0

for letter in sentence:
    if letter.isdigit():
        numbers+=1
    if letter.isalpha():
        letters+=1

print "LETTERS %s"%letters
print "NUMBERS %s"%numbers
