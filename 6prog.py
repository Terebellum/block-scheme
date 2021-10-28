#!/usr/bin/env python3
# -*- encoding: utf-8
import math
if __name__ == "__main__":
    S1 = float(input("S of triangle: "))
    S2 = float(input("S of circle: "))
    a = (4/(3**0.5)*S1)**0.5
    r = (S/pi)**0.5
    if r >= a/(3**0.5):
        print("Triangle in Circle")
    else:
        print("Triangle not in cirle")

    if r <= a/(2*(3**0.5)):
        print("Circle in triangle")
    else:
        print("Circle not in triangle")
