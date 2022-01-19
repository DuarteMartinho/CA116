#!/usr/bin/env python3

import os
files = os.listdir(".")

i = 0
while i < len(files):
    extension = files[i].split(".")
    with open("".join(files[i]), "r") as f_in:
        line = f_in.readline()
        if len(line.rstrip()) > 0:
            if len(extension) > 1:
                if extension[len(extension) - 1] == "py":
                    print(files[i])
    i = i + 1
