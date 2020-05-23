# -*- coding: utf-8 -*-
"""
Created on Tue May 19 10:10:29 2020

@author: Achyuth
"""

i=int(input('Enter the number of row -->'))
a=65
for _ in range(i):
    print()
    for d in range(_+1):
        print(chr(a),end=' ')
    a=a+1