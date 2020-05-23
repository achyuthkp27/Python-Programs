# -*- coding: utf-8 -*-
"""
Created on Fri May 22 09:11:17 2020

@author: Achyuth
"""

n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))