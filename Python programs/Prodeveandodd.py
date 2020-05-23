# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 08:36:06 2020

@author: Achyuth
"""

#produce even and odd numbers in given range
a=int(input("Enter start of the range"))
even=[]
odd=[]
b=int(input("Enter end of the range"))
for _ in range(a,b):
    if _%2==0:
        even.append(_)
    else:
        odd.append(_)
print(even)
print(odd)