# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 08:45:19 2020

@author: Achyuth
"""

n=int(input('ENTER NUMBER OF LINES:'))
print(n,end='\n\n')

for i in range(n):
  a,d,l=i+1,n-1,[]
  for j in range(i+1):
     m=' '*(-(len(str(a))-2)) + str(a)
     l.append(m)
     a,d =a+d,d-1
  print('  '.join(l[ : :-1]))