# -*- coding: utf-8 -*-
"""
Created on Tue May 19 08:48:25 2020

@author: Achyuth
"""

i=input("Enter a string-->")
for _ in range(len(i)):
    for a in range(_+1):
        print(i[a],end='')
    print()