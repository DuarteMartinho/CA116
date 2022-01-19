#!/usr/bin/env python3

side1 = int(input())
side2 = int(input())
side3 = int(input())

if side1 == side2 or side2 == side3 or side1 == side3:
    print("yes")
else:
    print("no")
