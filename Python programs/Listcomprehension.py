# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 09:24:51 2020

@author: Achyuth
"""

'''Let's learn about list comprehensions! You are given three integers x,y and z 
representing the dimensions of a cuboid along with an integer n.
You have to print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to .
 Here,-0<=i<=x,0<=j<=y,o<=k<=z 

Input Format

Four integers x,y,z and n  each on four separate lines, respectively.

Constraints

Print the list in lexicographic increasing order.

Sample Input 0

1
1
1
2
Sample Output 0

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]'''
x = int(input())
y = int(input())
z = int(input())
n = int(input())
print([ [ i, j,k ] for i in range( x + 1) for j in range( y + 1) for k in range( z + 1)  if (( i + j+k ) != n )])