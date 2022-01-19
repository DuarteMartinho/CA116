#!/usr/bin/env python3

if __name__ == "__main__":
    a = ["", "", "dog", "", "", "cat", "", "", "", "mouse"]

answer = ""
i = 0

while i < len(a):
    if a[i] != "":
        answer = a[i]
        i = len(a)
    i += 1

if answer != "":
    print(answer)
