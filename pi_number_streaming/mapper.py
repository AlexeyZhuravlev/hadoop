#!/usr/bin/env python2

import sys

for line in sys.stdin:
    a, b = list(map(float, line.split()))
    if a ** 2 + b ** 2 <= 1:
        print '%s\t%s' % ("I", 1)
    else:
        print '%s\t%s' % ("O", 1)
