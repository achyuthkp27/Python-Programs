# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 17:52:18 2020

@author: Achyuth
"""
import string
import random

def generate_password(theLength):
    ''' This function generates password '''
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation
    totalChars = letters + digits + punctuation
    finalResult = ""

    for i in range(theLength):
        finalResult += random.choice(totalChars)

    return finalResult


def main():
    
    while True:
        print("Enter the password length")
        theLength = input()

        try:
            theLength = int(theLength)
        except:
            print("Wrong password length!")
            continue

        thePassword = generate_password(theLength)
        print("The password is " + thePassword)

main()
