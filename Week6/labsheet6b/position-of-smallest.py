#!/usr/bin/env python3

if __name__ == "__main__":
    a = [49, 32, 39, 13, 30, 12, 14, 19, 31, 31]

x = 0
i = 0
while i < len(a) - 1:
    if x == 0:
        if a[i + 1] < a[i]:
            x = i + 1
    else:
        if a[i + 1] < a[x]:
            x = i + 1
    i += 1
print(x)
