# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:09:28 2020

@author: Achyuth
"""

import string


def var(a):
    a.reverse()
    c = string.punctuation
    e = [i for i in a if i not in c]
    f = "".join(e)
    if "9" in f:
        f = f.replace("9", "nine")
    if "8" in f:
        f = f.replace("8", "eight")
    if "7" in f:
        f = f.replace("7", "seven")
    if "6" in f:
        f = f.replace("6", "six")
    if "5" in f:
        f = f.replace("5", "five")
    if "4" in f:
        f = f.replace("4", "four")
    if "3" in f:
        f = f.replace("3", "three")
    if "2" in f:
        f = f.replace("2", "two")
    if "1" in f:
        f = f.replace("1", "one")
    if "0" in f:
        f = f.replace("0", "zero")
    print(f)


l = list(input())
var(l)
