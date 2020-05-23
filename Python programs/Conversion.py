# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 20:16:22 2020

@author: Achyuth
"""

# Python program to convert decimal into other number systems
dec = int(input("Enter a decimal value"))

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")