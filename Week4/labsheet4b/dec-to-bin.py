#!/usr/bin/env python3

numIn = int(input())
total = ""

j = 'start'
PowerTwo = 0
while j != 'end':
    if numIn > (2 ** PowerTwo):
        if numIn == (2 ** (PowerTwo + 1)):
            PowerTwo = PowerTwo + 1
            j = 'end'
        elif numIn < (2 ** (PowerTwo + 1)):
            j = 'end'
        else:
            PowerTwo = PowerTwo + 1

n = PowerTwo + 1
i = 0
while i < n:
    num = numIn // (2 ** PowerTwo)
    num2 = numIn % (2 ** PowerTwo)
    numIn = num2
    total = total + str(num)
    PowerTwo = PowerTwo - 1
    i += 1
print(int(total))
