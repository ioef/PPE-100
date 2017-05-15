#!/usr/bin/env python
'''
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
'''

sentences = []
while True:
    text = raw_input("Please write a sentence:")
    text = text.upper()
    
    if text:
         sentences.append(text.upper())
    else:
         break

for line in sentences:
    print line
