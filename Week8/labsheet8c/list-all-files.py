#!/usr/bin/env python3

import os
original_folder = os.listdir(".")
files = original_folder
folders = []
path = "./"
done = False

while not done:
    if len(files) > 0:
        i = 0
        isFolder = os.path.isdir(path + files[i])
        isFile = os.path.isfile(path + files[i])
    elif len(folders) > 0:
        j = 0
        path = path + folders[j] + "/"
        files = os.listdir(path)
        folders.pop(j)
        isFolder = False
        isFile = False
        j += 1

    if len(files) == 0 and len(folders) == 0:
        done = True
    else:
        if isFolder:
            folders.append(files[i])
            files.pop(i)
        elif isFile:
            print(path + files[i])
            files.pop(i)
    i += 1
