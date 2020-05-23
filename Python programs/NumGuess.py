# -*- coding: utf-8 -*-
"""
Created on Fri May  1 20:19:24 2020

@author: Achyuth
"""

while True:
    i=input("Do you want to play?y/n\n-->")
    if i=='n':
        break
    a=int(input("Guess the number(1 0r 2)-->"))
    from random import randrange
    if a==randrange(1,3):
        print("Wow! your guess is perfect")
    else:
        print("wrong guess\nTry again")