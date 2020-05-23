# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 20:16:23 2020

@author: Achyuth
"""

# Program to check Armstrong numbers in a certain interval

lower = int(input("enter start range"))
upper = int(input("enter end range"))
if lower>upper:
    lower,upper=upper,lower
for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)