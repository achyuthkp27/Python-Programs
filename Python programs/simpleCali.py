# -*- coding: utf-8 -*-
"""
Created on Fri May  1 20:24:28 2020

@author: Achyuth
"""

while True:
    i=input('Press y to continue\n')
    if i!='y':
        break
    a,b=map(int,input("enter 1st numbers\n").split())
    c={1:a+b,2:a-b,3:a*b,4:a/b}
    print(c.get(int(input("Enter choice\n1.Add\n2.Sub\n3.Mul\n4.Div\n")),'Invalid choice'))