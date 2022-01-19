#!/usr/bin/env python3

import os
files = os.listdir(".")
shebang = "#!/usr/bin/env python3"
i = 0
while i < len(files):
    extension = files[i].split(".")
    print(extension)
    with open("".join(files[i]), "r") as f_in:
        line = f_in.readline()
        if line.rstrip() == shebang:
            print(files[i])
        elif len(line.rstrip()) > 0 and len(extension) > 1:
            if extension[len(extension) - 1] == "py":
                print(files[i])
    i = i + 1
