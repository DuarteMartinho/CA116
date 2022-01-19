#!/usr/bin/env python3

import sys
lineIn = sys.stdin.readlines()
sentence = ""
dict_fullstop = {
    ",": "\n",
}

i = 0
while i < len(lineIn):
    eachLine = lineIn[i].split()
    pageNumber = eachLine[0]
    line = int(eachLine[1])
    character = int(eachLine[2])
    file_name = "page-" + pageNumber + ".txt"
    with open(file_name, "r") as f_in:
        lines = f_in.read().split("\n")
        selectedLine = lines[line]
        if character == len(selectedLine):
            selectedChar = ""
        else:
            selectedChar = selectedLine[character]
        sentence += selectedChar
        if selectedChar in dict_fullstop:
            sentence += dict_fullstop[selectedChar]
    i += 1
print(sentence)
