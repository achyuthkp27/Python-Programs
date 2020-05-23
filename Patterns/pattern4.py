# -*- coding: utf-8 -*-
"""
Created on Tue May 19 09:07:43 2020

@author: Achyuth
"""

i=int(input('Enter the number of rows-->'))

for _ in range(i+1):
    for a in range(_+1):
        print('\t'*(10-a))
        print('*'*a,end='')
    print()