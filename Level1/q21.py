#!/usr/bin/env python
'''
Print the ordinal values of the characters consisting a given string.
For example if we print the ordinal values of the string "Hello World"
the Result should be like the following:
The ordinal value of character H is 72
The ordinal value of character e is 101
The ordinal value of character l is 108
The ordinal value of character l is 108
The ordinal value of character o is 111

As bonus you may also print the hex and the binary values.
'''

text = "Hello World! Python is Great!"

for ch in text:
    #calculate the ASCII ordinal value
    ordinal = ord(ch)
    #calculate the hex value
    hexadecimal = hex(ord(ch))
    binary = bin(ord(ch))

    print "The character {0} has\t ordinal:{1}\t\thex: {2}\t and binary: {3}".format(ch,ord(ch), hexadecimal, binary)

