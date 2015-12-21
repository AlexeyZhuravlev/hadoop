#!/usr/bin/env python2

import sys

total = 0
success = 0

for line in sys.stdin:
    answer, count = line.split()
    if answer == "I":
        success += int(count)
    total += int(count)

print (4 * float(success) / float(total))
