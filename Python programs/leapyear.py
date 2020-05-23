# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 08:37:10 2020

@author: Achyuth
"""
# Python program to check if year is a leap year or not


year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
