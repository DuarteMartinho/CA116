#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())

isEvenOrOdd = c % 2

print(a - (a * isEvenOrOdd) + (b * isEvenOrOdd))
