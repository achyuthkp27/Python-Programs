# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 20:16:23 2020

@author: Achyuth
"""

# Program to display calendar of the given month and year

# importing calendar module
from calendar import month


yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# display the calendar
print(month(yy, mm))