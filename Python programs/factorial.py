# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 08:24:31 2020

@author: Achyuth
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))

'''There is a inbuilt function in python to find factorial of a number
factorial()'''