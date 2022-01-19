#!/usr/bin/env python3

addition = input()
i = 0
j = 0
total = 0
k = -1
while i < 5:
    j = j + 1
    while j < len(addition) and addition[j] != "+":
        j += 1
    total = total + int(addition[k + 1:j])
    k = j
    i += 1
print(total)
