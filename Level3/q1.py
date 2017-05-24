#!/usr/bin/env python
'''
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
import re

data = [ x for x in raw_input("Give Passwords:").split(',')]


goodPassList =[]

for password in data:
    #check if password length is between 6 and 12 characters
    if len(password) >=6 and len(password) <=12:
       #At least 1 letter between [a-z]
        if re.search('[a-z]',password):
            #At least 1 number between [0-9]
            if re.search('[0-9]',password):
                #At least 1 letter between [A-Z]
                if re.search('[A-Z]',password):
                    #At least 1 character from [$#@]
                    if re.search('[$#@]',password):
                        #since password passed all tests append it to the good password list
                        goodPassList.append(password)
          

print ' '.join(goodPassList)
