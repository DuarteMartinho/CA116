#!/usr/bin/env python3

numIn = int(input())


x1 = numIn // 100
x2 = (numIn // 10) - (x1 * 10)
x3 = (numIn) - ((numIn // 10) * 10)

print(x1)
print(x2)
print(x3)
