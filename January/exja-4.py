#!/usr/bin/env python3

import sys
lines = sys.stdin.read().split('"')

if len(lines) > 2:
    print(lines[1])
