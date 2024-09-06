#!/usr/bin/python3

for upper_ASCII in range(65, 90):
    if upper_ASCII != 101 and upper_ASCII != 113:
        print("{}".format(chr(upper_ASCII)), end="")
