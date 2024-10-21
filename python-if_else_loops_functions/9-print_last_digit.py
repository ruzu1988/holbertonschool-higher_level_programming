#!/usr/bin/python3
def print_last_digit(number):
    lastdg = abs (number) % 10
    print("{}".format(lastdg), end="")
    return lastdg
