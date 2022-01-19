#!/usr/bin/env python3

numIn = int(input())
total = ""

j = 'start'
PowerSixTeen = 0
while j != 'end':

    if numIn > (16 ** PowerSixTeen):

        if numIn == (16 ** (PowerSixTeen + 1)):
            PowerSixTeen = PowerSixTeen + 1
            j = 'end'

        elif numIn < (16 ** (PowerSixTeen + 1)):
            j = 'end'

        else:
            PowerSixTeen = PowerSixTeen + 1


n = PowerSixTeen + 1
i = 0
while i < n:

    num = numIn // (16 ** PowerSixTeen)
    num2 = numIn % (16 ** PowerSixTeen)

    numIn = num2

    if num == 10:
        num = "a"
    elif num == 11:
        num = "b"
    elif num == 12:
        num = "c"
    elif num == 13:
        num = "d"
    elif num == 14:
        num = "e"
    elif num == 15:
        num = "f"

    total = total + str(num)

    PowerSixTeen = PowerSixTeen - 1

    i += 1

print(total)
