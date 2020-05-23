# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 08:35:37 2020

@author: Achyuth
"""

#Simple calculator
def read():
    return int(input("Enter a number"))
def calculate(a,b,c=0):
    if c==0:
        print(a+b)
    elif c==1:
        print(a-b)
    elif c==2:
        print(a*b)
    elif c==3:
        print(a/b)
    elif c==4:
        print(a//b)
    elif c==5:
        print(a%b)
    else:
        print("Invalid choice")
def choice():
    print("Enter your choice\n0.addition\t1.subtraction\t2.multiplication\n3.division\t4.flooring\t5.modulo")
    return int(input())
def main():
    calculate(read(),read(),choice())
main()