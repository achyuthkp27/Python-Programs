# -*- coding: utf-8 -*-
"""
Created on Tue May 19 09:19:53 2020

@author: Achyuth
"""

i=int(input('Enter the number of rows-->'))

for _ in range(i):
    print(' '*(i-_),end='')
    for a in range(_+1):
        print('*',end='')
    print()