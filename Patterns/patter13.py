# -*- coding: utf-8 -*-
"""
Created on Thu May 21 09:38:45 2020

@author: Achyuth
"""

def staircase(n):
    for i in range(1, n + 1):
       print(' ' * (n - i) + '#' * i)
            
if __name__ == '__main__':
    n = int(input())
    staircase(n)