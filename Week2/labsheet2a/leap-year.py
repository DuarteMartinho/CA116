#!/usr/bin/env python3

year = int(input())

leapYear = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

print(leapYear)
