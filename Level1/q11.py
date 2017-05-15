#!/usr/bin/env python

def compStrings (str1, str2):
    if len(str1) > len(str2):
        print str1
    elif len(str1) < len(str2):
        print str2
    else:
        print str1
        print str2


compStrings("test12345", "test123456")


