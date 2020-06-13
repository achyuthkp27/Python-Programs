# -*- coding: utf-8 -*-
"""
Created on Sat May 30 09:22:45 2020

@author: Achyuth
"""

import re

previous = 0
run = True
print('You Need to Multiply the equation wih zero before quiting')
def MagicalCalci():
    global run, previous
    equation=' '
    if previous==0:
        equation=input('Enter the equation ')
    else:
        equation=input(str(previous))
        
    if equation== 'quit':
        run=False
    else:
        equation=re.sub('[a-zA-Z,.:()" "]', '',equation)
        
    if previous==0:
        previous=eval(equation)
    else:
        previous=eval(str(previous)+equation)

while run:
    MagicalCalci()