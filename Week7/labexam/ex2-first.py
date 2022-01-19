#!/usr/bin/env python3

s = input()

musical_notes = "abcdefg"

i = 0
while i < len(s):
    j = 0
    while j < len(musical_notes):
        if s[i] == musical_notes[j]:
            print(s[i])
            j = len(musical_notes)
            i = len(s)
        j = j + 1
    i = i + 1
