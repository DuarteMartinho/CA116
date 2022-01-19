#!/usr/bin/env python3

number = int(input())
digitWanted = int(input())

number = number // (10 ** digitWanted) % 10
print(number)
