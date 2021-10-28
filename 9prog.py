#!/usr/bin/env python3
# -*- encoding: utf-8
if __name__ == "__main__":
    a = float(input())
    b = float(input())
    c = float(input())
    x = float(input())
    y = float(input())
    if (a > b):
        am = b
        if (a > c):
            bm = c
        else:
            bm = a
    else:
        am = a
        if (b > c):
            bm = c
        else:
            bm = b
    
    if ((x > am and y > bm) or (x > bm and y > am)):
        print("Влезает")
    else:
        print("Не влезает")
