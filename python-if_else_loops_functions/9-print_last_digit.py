#!/usr/bin/python3
def print_last_digit(number):
    lastdg = abs (number) % 10 #-obtiene el valor absoluto del # -no afecta si es neg
    print("{}".format(lastdg), end="")
    return lastdg
