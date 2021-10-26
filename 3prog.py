#!/usr/bin/env python3
# -*- encoding: utf-8
if __name__ == "__main__":
    x = float(input("x?"))
    y = float(input("y?"))
    R1 = float(input("R1?"))
    R2 = float(input("R12"))
    r = (x**2+y**2)**0.5
    if (r > R1) and (r < R2):
        print("Принадлежит")
    else:
        print("Не принадлежит")
