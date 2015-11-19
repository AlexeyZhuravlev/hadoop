#!/usr/bin/env python2

import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for i in words:
        q = ''
        for c in i:
            if str.isalpha(c):
                 q = q + c
        q = str.lower(q)
        if q != '' and q[0] == 'a':
            print '%s\t%s' % (q, 1)
