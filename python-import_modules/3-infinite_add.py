#!/usr/bin/python3
import sys
if __name__ == "__main__":
    total = 0
    argv = sys.argv[1:]
    for arg in argv:
        total += int(arg)
    print("{}".format(total))
