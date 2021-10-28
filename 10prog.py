#!/usr/bin/env python3
# -*- encoding: utf-8
if __name__ == "__main__":
    t = float(input())
    if (t > 0):
        if (t % 5 >= 3):
            print("Red")
        else:
            print("Green")
    else:
        print("No answers")
