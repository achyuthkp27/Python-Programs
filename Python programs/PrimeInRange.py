# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 20:06:27 2020

@author: Achyuth
"""

# Python program to display all the prime numbers within an interval

lower = int(input("Enter start range"))
upper = int(input("Enter end range"))
if lower>upper:
    upper,lower=lower,upper
print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)