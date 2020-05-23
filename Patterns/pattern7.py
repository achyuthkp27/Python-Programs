# -*- coding: utf-8 -*-
"""
Created on Tue May 19 09:49:32 2020

@author: Achyuth
"""

i=int(input('Enter the number of rows-->'))
a=1
for _ in range(i):
    print(' '*(i-_+1),end='')
    print('*'*a,end='\n')
    a=a+2
a=a-3
for _ in range(i+1):
    print(' '*(_+2),end='')
    print('*'*(a+1),end='\n')
    a=a-2