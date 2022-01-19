#!/usr/bin/env python3

a = [32011, 22512, 4901, 21873, 15992]
total = 0

i = 0
while i < len(a):
   total = total + (int(input()) - a[i])
   i = i + 1

print(total)