#!/usr/bin/env python3

hyp = int(input())
lenght1 = int(input())
lenght2 = int(input())

hypCheck = hyp ** 2
lenghtCheck = (lenght1 ** 2) + (lenght2 ** 2)

triangleProof = hypCheck == lenghtCheck

print(triangleProof)
