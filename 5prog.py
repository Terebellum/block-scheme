#!/usr/bin/env python3
# -*- encoding: utf-8
import math
if __name__ == "__main__":
    S1 = float(input("S of circle: "))
    S2 = float(input("S of square: "))
    d = ((S1/math.pi)**0.5)*2
    a = S2**0.5
    if d <= a:
        print("Круг может поместиться в квадрате")
    else:
        print("Круг не может поместиться в квадрате")

    if d >= a*2**0.5:
        print("Квадрат может поместиться в круге")
    else:
        print("Квадрат не может поместиться в круге")

        
