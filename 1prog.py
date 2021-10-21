#!/usr/bin/env python3
# -*- encoding: utf-8
if __name__ == "__main__":

    x = float(input("X coordinate: "))
    y = float(input("Y coordinate: "))
    R = float(input("R of circle: "))

    r = (x**2+y**2)**0.5
    if r < R:
        print("Point at Circle")
    else:
        print("Point not in Circle")
