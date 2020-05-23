# -*- coding: utf-8 -*-
"""
Created on Fri May  1 17:18:55 2020

@author: Achyuth
"""

#Die Rolling simulator
      
while True:
    i=input('Do you want to roll the die? y or n\n')
    if i=='n':
        break
    from random import randrange
    a=randrange(1,7)
    print('\n\n')
    s={1:'\n * \n',2:'\n* *\n',3:' * \n * \n * ',4:'* *\n\n* *',5:'* *\n * \n* *',6:'* *\n* *\n* *'}
    print(s.get(a,"Invalid Entry"))  