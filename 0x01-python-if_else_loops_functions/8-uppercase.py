#!/usr/bin/python3
def uppercase(string):
    for char in string:
        if ord(char) in range(97, 123):
            is_upper = ord(char)-32
            print("{}".format(chr(is_upper)), end='')
        else:
            print("{}".format(char))
