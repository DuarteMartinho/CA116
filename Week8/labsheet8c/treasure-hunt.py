#!/usr/bin/env python3

import os

with open("start.txt", "r") as f_in:
    readLine = f_in.readline()
    checkFile = os.path.isfile(readLine.rstrip())
    if checkFile:
        while checkFile:
            with open(readLine.rstrip(), "r") as f_in:
                readLine = f_in.readline()
                checkFile = os.path.isfile(readLine.rstrip())
    print(readLine.rstrip())