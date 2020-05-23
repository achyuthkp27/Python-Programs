# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 18:21:59 2020

@author: Achyuth
"""
from random import randrange
def rolling(c):
    if c==1:
        print("|   |\n| * |\n|   |\n")
    elif c==2:
        print("| * |\n|   |\n| * |\n")
    elif c==3:
        print("| * |\n| * |\n| * |\n")
    elif c==4:
        print("|* *|\n|   |\n|* *|\n")
    elif c==5:
        print("|* *|\n| * |\n|* *|\n")
    elif c==6:
        print("|* *|\n|* *|\n|* *|\n")
    else:
        print("Invalid roll\n")
def roll():
    return randrange(1,7)
rolling(roll())