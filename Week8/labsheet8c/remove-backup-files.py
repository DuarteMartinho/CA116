#!/usr/bin/env python3

import os
files = os.listdir(".")

i = 0
while i < len(files):
    extension = files[i].split(".")
    if len(extension) > 1:
        check_file = os.path.isfile("".join(files[i]))
        if extension[len(extension) - 1] == "bak" and check_file:
            os.unlink("".join(files[i]))
    i = i + 1
