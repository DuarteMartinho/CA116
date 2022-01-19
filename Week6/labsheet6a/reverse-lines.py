#!/usr/bin/env python3

#!/usr/bin/env python3

s = input()
a_list = []

while s != "end":
    a_list.append(s)
    s = input()

i = 0
while i < len(a_list):
    print(a_list[len(a_list) - i - 1])
    i += 1
