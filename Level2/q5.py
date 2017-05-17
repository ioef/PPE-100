#!/usr/bin/env python
'''
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data.
'''


words = raw_input("Provide a number of words with whitespaces:")

splitted_words = [ word for word in words.split(" ")]

#order the list
splitted_words.sort()

#remove duplicates by transforming it to a set
final_set = set(splitted_words)

print ' '.join(final_set)
