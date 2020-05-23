# -*- coding: utf-8 -*-
"""
Created on Tue May 19 09:42:24 2020

@author: Achyuth
"""
i=int(input('Enter the number of rows-->'))
a=1
for _ in range(i):
    print(' '*(i-_+1),end='')
    print('*'*a,end='\n')
    a=a+2