# -*- coding: utf-8 -*-
"""
Created on Fri May  1 20:47:10 2020

@author: Achyuth
"""
c=[]
n=int(input('enter a number'))
a,b=0,1
while a<n:
    c.append(a)
    a,b=b,a+b
print(c)
print(c[::-1])
