#!/usr/bin/env python3

import sys
text_in = sys.stdin.readlines()

with open("banned.txt", "r") as ban_in:
    banned = ban_in.readlines()

banned_words = {}
i = 0
while i < len(banned):
    banword = banned[i].rstrip()
    banned[i] = banword
    banned_words[banword] = len(banword)
    i += 1

i = 0
while i < len(text_in):
    line = text_in[i].rstrip().split()
    j = 0
    while j < len(line):
        if line[j] in banned_words:
            line[j] = banned_words[line[j]] * "*"
        j += 1
    line_out = " ".join(line)
    print(line_out)
    i += 1
