# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 08:59:54 2020

@author: Achyuth
"""
mary=(10+12+14)/3 #average marks scored in a match
john=(15+10+9)/3
joseph=(12+12+15)/3
if mary>john and mary>joseph:
    print("Mary won the match")
elif mary==john or mary==joseph:
        print("draw")
elif john>joseph:
    print("John won the match")
elif john==joseph:
    print("Draw between john and joseph")
else:
    print("Joseph won the match")