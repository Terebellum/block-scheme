#!/usr/bin/env python3
# -*- encoding: utf-8
if __name__ == "__main__":
    a = float(input())
    b = float(input())
    c = float(input())
    if (a == 0):
        print("No solve")
    else:
        D = b**2-4*a*c
        if (D > 0):
            x1 = (0-b+D**0.5)/2*a
            x2 = (0-b-D**0.5)/2*a
            print("X1 is ", x1)
            print("X2 is ", x2)
        elif(D == 0):
            x = -b/2*a
            print("X is ", x)
        else:
            print("No answers")
