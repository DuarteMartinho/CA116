#!/usr/bin/env python3

import sys
file_name = sys.argv[1]

with open(file_name, "w") as f:
   f.write("Hello world.\n")
