#!/usr/bin/env python3

import sys
names = sys.stdin.readlines()

names_dict = {}
with open("boys.txt", "r") as f_in:
    boys = f_in.readlines()
    i = 0
    while i < len(boys):
        boy_name = boys[i].rstrip()
        if boy_name not in names_dict:
            names_dict[boy_name] = "boy"
        i += 1
    with open("girls.txt", "r") as f_in2:
        girls = f_in2.readlines()
        i = 0
        while i < len(girls):
            girl_name = girls[i].rstrip()
            if girl_name not in names_dict:
                names_dict[girl_name] = "girl"
            else:
                names_dict[girl_name] = "either"
            i += 1

i = 0
while i < len(names):
    nameIn = names[i].rstrip()
    if nameIn in names_dict:
        print(nameIn, names_dict[nameIn])
    i += 1
