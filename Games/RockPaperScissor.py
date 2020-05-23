# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 08:29:07 2020

@author: Achyuth
"""
import random

def game():
    game_list = ["R", "P", "S"]

    print("WELCOME TO snake, water, gun game")
    print("R--Rock")
    print("P--Paper")
    print("S--scissor")
    name = input("Enter your name:").upper()
    h_p = 0
    c_p = 0
    print("Best of Three")
    for i in range(3):
        h_c = input("Enter your choice:").upper()
        c_c = random.choice(game_list)
        if h_p == 10 or c_p == 10:
            break
        while 1:
            if h_c == "R" or h_c == "P" or h_c == "S":
                break
            else:
                print("Wrong input....Try again")
                h_c = input("Enter your choice:").upper()
        print(".....", c_c)
        if h_c == c_c:
            print("0 points added")
        elif h_c == "R" and c_c == "S":
            print("1 point added to", name)
            h_p += 1
        elif h_c == "P" and c_c == "R":
            print("1 point added to", name)
            h_p += 1
        elif h_c == "S" and c_c == "P":
            print("1 point added to", name)
            h_p += 1
        else:
            print("1 point added to COMPUTER")
            c_p += 1

    print("HUMAN SCORED----", h_p, "COMPUTER SCORED----", c_p)
    if h_p > c_p:
        print(name, "Won the match")
    else:
        print("Computer won the match")

    print()
    while 1:
        try:
            take = int(input("Enter:"))
            break

        except:
            print("Error...Enter again")
    return take


while 1:
    value = game()
    if value == 1:
        game()
    else:
        print("Bye!see you later...")