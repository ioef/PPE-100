#!/usr/bin/env python
'''
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200
'''

amount = 0

while True:
    in_text = raw_input("Provide Command:")

    if in_text:
        split_text = in_text.split(" ")
        if split_text[0] == "D":
            amount += int(split_text[1])
        elif split_text[0] =="W":
            amount -= int(split_text[1])
        else:
            pass
  
    else:
        break

print ("The total amount in your account is %s"%amount)

