#!/usr/bin/env python3

with open("irish-dobs.txt", "r") as f_in:
    x = f_in.readlines()
    with open("american-dobs.txt", "w") as f_out:
        i = 0
        while i < len(x):
            line = x[i]
            split_line = line.split()
            split_date = split_line[0].split("/")
            tmp = split_date[1]
            split_date[1] = split_date[0]
            split_date[0] = tmp
            date_join = "/".join(split_date)
            name_join = " ".join(split_line[1:])
            f_out.write(date_join + " " + name_join + "\n")
            i += 1
