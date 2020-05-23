# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 20:06:27 2020

@author: Achyuth
"""

# Multiplication table (from 1 to 10) in Python

num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)