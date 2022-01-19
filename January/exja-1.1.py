#!/usr/bin/env python3

i = 0
while i < len(a):
   if a[i] < 0:
      digit = 7  # 3 is wrong here
   else:
      digit = 3
   if a[i] % 10 == digit:
      print(a[i])
   i = i + 1
