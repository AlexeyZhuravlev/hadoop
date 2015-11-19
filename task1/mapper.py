#!/usr/bin/env python2

import sys

def read_input(file):
    for line in file:
        yield line.split()

def main():
    for x in sys.stdin.readlines():
        for i in x.split():
            q = ''
            for c in i:
                if str.isalpha(c):
                    q = q + c
            if q != '' and q[0] == 'A':
                print(str.lower(q) + '\t' + str(1))

if __name__ == "__main__":
    main()
