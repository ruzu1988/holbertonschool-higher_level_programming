#!/usr/bin/python3
def uppercase(str):
    for letra in str:
        if 'a' <= letra <= 'z':
            letra_mayus = chr(ord(letra) - 32)
        else:
            letra_mayus = letra
        print("{}".format(letra_mayus), end="")
    print()
