#!/usr/bin/env python3

if __name__ == "__main__":
    a = ["mountain", "montagne", "mont", "mo", "montages", "zebra", "monthly"]
    s = "mont"

prefixWord = s
prefixLen = len(s)

i = 0
while i < len(a):
    word = a[i]
    if word[:prefixLen] == prefixWord:
        print(a[i])
    i += 1
