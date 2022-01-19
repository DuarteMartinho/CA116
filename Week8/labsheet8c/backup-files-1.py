#!/usr/bin/env python3

import os
files = os.listdir(".")

i = 0
while i < len(files):
    extension = files[i].split(".")
    if len(extension) > 1:
        if extension[len(extension) - 1] != "bak":
            with open("".join(files[i]), "r") as f_in:
                data = f_in.read()
                with open("".join(files[i]) + ".bak", "w") as f_out:
                    f_out.write(data)
    i = i + 1
