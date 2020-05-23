# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 08:26:10 2020

@author: Achyuth
"""
a=eval(input("Enter your first number-"))
b=eval(input("Enter your second number-"))
c=eval(input("Enter your third number-"))
if a>=b and a>=c:
    print("First Number is bigger")
elif b>=c:
    print("Second Number is bigger")
else:
    print("Third Number is bigger")