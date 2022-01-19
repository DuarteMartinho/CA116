#!/usr/bin/env python3

timetable = []

s = input()
while s != "end":
    timetable.append(s)
    s = input()

i = 0
while i < len(timetable):
    line = timetable[i]
    line_list = line.split()
    start_hour = int(line_list[1])
    total_hour = int(line_list[2])
    end_hour = start_hour + (total_hour - 1)
    line_list[1] = str(start_hour) + ":00"
    line_list[2] = str(end_hour) + ":50"
    line_join = " ".join(line_list)
    print(line_join)
    i += 1
