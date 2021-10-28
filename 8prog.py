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
            y1 = (0-b+D**0.5)/2*a
            y2 = (0-b-D**0.5)/2*a
            if y1 >= 0 and y2 >= 0:
                x1 = y1**0.5
                x2 = 0 - (y1**0.5)
                x3 = y2**0.5
                x4 = 0 - (y2**0.5)
                print("X1 is ", x1)
                print("X2 is ", x2)
                print("X3 is ", x3)
                print("X4 is ", x4)
            elif y1 < 0 and y2 >= 0:
                x1 = y2**0.5
                x2 = 0 - (y2**0.5)
                print("X1 is ", x1)
                print("X2 is ", x2)
            elif y1 >= 0 and y2 < 0:
                x1 = y1**0.5
                x2 = 0 - (y1**0.5)
                print("X1 is ", x1)
                print("X2 is ", x2)
            elif y1 < 0 and y2 < 0:
                print("No answers")
                
        elif(D == 0):
            y = -b/2*a

            x1 = y**0.5
            x2 = 0 - (y**0.5)
            print("X1 is ", x1)
            print("X2 is ", x2)
        else:
            print("No answers")
