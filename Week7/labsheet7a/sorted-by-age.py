#!/usr/bin/env python3

s = input()
a = []

while s != "end":
    a.append(s)
    s = input()

i = 0
while i < len(a):
    j = i + 1
    while j < len(a):
        term = a[i]
        sliceYear = int(term[6:8])
        sliceMonth = int(term[3:5])
        sliceDay = int(term[:2])

        term2 = a[j]
        sliceYear2 = int(term2[6:8])
        sliceMonth2 = int(term2[3:5])
        sliceDay2 = int(term2[:2])

        if sliceYear > sliceYear2:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
        elif sliceYear == sliceYear2:
            if sliceMonth > sliceMonth2:
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp
            elif sliceMonth == sliceMonth2:
                if sliceDay > sliceDay2:
                    tmp = a[i]
                    a[i] = a[j]
                    a[j] = tmp
        j = j + 1
    i += 1

i = 0
while i < len(a):
    term = a[i]
    print(term[9:])
    i += 1
