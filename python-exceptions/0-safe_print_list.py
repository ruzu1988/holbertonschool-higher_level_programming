#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for idx in range(x):
        try:
            print(my_list[idx], end="")
            count += 1
        except: continue
    print()
    return count
