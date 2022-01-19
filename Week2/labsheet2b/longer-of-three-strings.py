#!/usr/bin/env python3

phrase1 = input()
phrase2 = input()
phrase3 = input()

if (len(phrase1) > len(phrase2) and (len(phrase1) > len(phrase3))):
    print(phrase1)
elif (len(phrase2) > len(phrase1) and (len(phrase2) > len(phrase3))):
    print(phrase2)
else:
    print(phrase3)
