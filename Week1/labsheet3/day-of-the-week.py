#!/usr/bin/env python3

monthIn = int(input())
daysIn = int(input())

month = 30 * (monthIn - 1)
days = daysIn - 1
DayOfYear = days + month

DayOfWeek = DayOfYear % 7 + 1

print(DayOfWeek)
