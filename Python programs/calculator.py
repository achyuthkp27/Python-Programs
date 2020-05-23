# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 08:26:33 2020

@author: Achyuth
"""

'''This program is used to calculate few Mathematical operations'''
from math import *
def read():
    return eval(input("Enter value "))
def calci(c,a,b):
    if c==1:
        print(f"Addition of {a} and {b}=",a+b)
    elif c == 2:
        print(f"Difference of {a} and {b}=", a - b)
    elif c==3:
        print(f"Product of {a} and {b}=",a*b)
    elif c==4:
        print(f"Quotient of {a} and {b}=",a/b)
    elif c==5:
        print(f"Square root of {a} ",sqrt(a))
        print(f"Square root of {b} ", sqrt(b))
    elif c==6:
        print(f"Factorial of {a} ",factorial(a))
        print(f"Factorial of {b} ", factorial(b))
    elif c==7:
        print(f"Perfect Quotient of {a} and {b}=",a//b)
    elif c==8:
        print(f"Modulus of {a} and {b}=",a%b)
    elif c==9:
        print(f"GCD of {a} and {b}=",gcd(a,b))
    elif c==10:
        print(f"Celi of {a}=",ceil(a))#This function returns the smallest integral value greater than the number. If number is already integer, same number is returned.
        print(f"Celi of {b}=", ceil(b))
    elif c == 11:
        print(f"floor of {a}=", floor(a))#This function returns the greatest integral value smaller than the number. If number is already integer, same number is returned.
        print(f"floor of {b}=", floor(b))
    elif c==12:
        print(f"Absolute of {a}=",fabs(a))
        print(f"Absolute of {b}=", fabs(b))
    elif c==13:
        print(f"power of {a}  raise {b}=",pow(a,b))
    elif c==14:
        print(f"expo of {a}=",exp(a))#This function returns the logarithmic value of a with base b. If base is not mentioned, the computed value is of natural log.
        print(f"expo of {b}=", exp(b))
    elif c==15:
        print(f"Log of {a} and {b}=",log(a,b)) #This function returns the logarithmic value of a with base b. If base is not mentioned, the computed value is of natural log.
    else:
        print("Invalid Choice")
def choice():
    print("Enter your Choice\n1.Add\t2.Sub\t3.Mul\n4.Div\t5.Sqrt\t6.fatorial")
    print("7.Flooring(division)\t8.modulo\t9.GCD\n10.celi(give float value)\t11.floor(give float value)\t12.fabs")
    print("13.Power\t14.exponential\t15.logorithm\n")
    return int(input())
calci(choice(),read(),read())
