#!/usr/bin/env python3

import os
files = os.listdir(".")

i = 0
while i < len(files):
    extension = files[i].split(".")
    if len(extension) > 1:
        if extension[len(extension) - 1] == "py":
            print(files[i])
    i = i + 1
