# -*- coding: utf-8 -*-
"""
Created on Tue May 19 10:06:12 2020

@author: Achyuth
"""

i=int(input('Enter the number of row -->'))
a=1
for _ in range(i):
    for d in range(_+1):
        print(a,end=' ')
        a=a+1
    print()