# -*- coding: utf-8 -*-
"""
Created on Tue May 19 08:42:20 2020

@author: Achyuth
"""
i=0
a=input('Enter a String-->')
for _ in range (len(a)):
    print('\t'*i,end='')
    print(a[_])
    i=i+1