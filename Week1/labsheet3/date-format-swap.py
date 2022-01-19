#!/usr/bin/env python3

dateIn = int(input())

dateSplitDay = (dateIn % 10000) // 100
dateSplitMonth = (dateIn // 100) // 100
dateSplitYear = (dateIn % 100)

dateSwapped = (dateSplitDay * 10000) + (dateSplitMonth * 100) + (dateSplitYear)

print(dateSwapped)
