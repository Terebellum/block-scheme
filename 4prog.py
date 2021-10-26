#!/usr/bin/env python3
# -*- encoding: utf-8
if __name__ == "__main__":
    numofmonth = int(input("Enter a number of month(1-12)"))
    if (numofmonth < 1) or (numofmonth > 12):
        print("Not a month")
    elif (numofmonth > 2) and (numofmonth < 6):
        print("Spring")
    elif (numofmonth > 5) and (numofmonth < 9):
        print("Summer")
    elif (numofmonth > 8) and (numofmonth < 12):
        print("Autumn")
    else:
        print("Winter")
