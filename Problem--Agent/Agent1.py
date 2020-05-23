# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 13:40:42 2020

@author: Achyuth
"""

#Solution 2
dictionary={'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
encrypted=input()
flipencrypted=encrypted[::-1]
for i in flipencrypted:
    if not i.isalnum():
        flipencrypted=flipencrypted.replace(i,"")
for i in flipencrypted:
    if i in dictionary:
        flipencrypted=flipencrypted.replace(i,dictionary[i])
print(flipencrypted)