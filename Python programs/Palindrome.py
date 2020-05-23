# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 08:34:19 2020

@author: Achyuth
"""

#check given number is palindrome or not
rev=0
a=int(input("Enter a Number "))
i=a
while a:
    rev=rev*10+a%10
    a=a//10
if i==rev:
    print("Given Number is a Palindrome number")
else:
    print("Given Number is not a Palindrome")