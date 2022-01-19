#!/usr/bin/env python3

import sys
file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1, "r") as f_in1:
    with open(file2, "r") as f_in2:
        lines = f_in1.readlines()
        lines2 = f_in2.readlines()
        found = False
        j = 0
        position = 0

        if len(lines) < len(lines2):
            smaller = len(lines)
        else:
            smaller = len(lines2)

        while j < smaller:
            sentence1 = lines[j].rstrip()
            sentence2 = lines2[j].rstrip()
            i = 0
            while i < len(sentence1):
                if sentence1[i] != sentence2[i]:
                    line = j
                    position = i
                    found = True
                    j = len(lines)
                    i = len(sentence1)
                i += 1
            j += 1
        if not found and lines != lines2:
            print(smaller, position)
        elif found:
            print(line, position)
