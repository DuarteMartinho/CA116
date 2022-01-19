#!/usr/bin/env python3

s = input()

#Get last digit
digit = len(s) - 1

#Define total
total = 0

i = 0
while i < len(s):
    # convert str to int and convert it to decimal
    number = int(s[digit]) * (2 ** i)
    # add to total
    total = total + number
    # get the digit before last until 0
    digit = digit - 1
    # increment loop
    i += 1
# print total
print(total)
