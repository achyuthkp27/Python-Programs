# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 13:21:42 2020

@author: Achyuth
"""

import sys

YourScore=0
TotalScore=0
carry=["p","j","c++"]
def quiz():
    global carry,TotalScore,YourScore
    inp=int(input("Which Quiz you Want to take\n1.Python Quiz\n2.Java Quiz\n3.c/C++ Quiz\n-->"))
    if inp==1:
        pyt(carry)
        try:
            carry.pop(0)
        except:
            pass
    elif inp==2:
        jav(carry)
        try:
            carry.pop(1)
        except:
            pass
    elif inp==3:
        cprog(carry)
        try:
            carry.pop(2)
        except:
            pass    
  
    else:
        print("Wrong entry")
    print(f"Your total Score={YourScore}")
    print(f"Total Quiz score{TotalScore}")
    del(inp)
    if len(carry)==0:
        sys.exit()
    p=input("Do you want to take another Quiz?y/n\n-->")
    if p.lower()=="y":
        pass
    else:
        sys.exit()
def pyt(a):
    global TotalScore,YourScore
    if "p" in a:
        print("Welcome to Python quiz")
        TotalScore+=8
        a1=int(input("""What the does random.seed(3) return?
1.True
2.None
3.3
4.1
-->"""))
        if a1==2:
            YourScore+=1
        else:
            print("Correct Answer=None")
        a2=int(input("""Which of the following cannot be returned by random.randrange(4)?
1) 0
2) 3
3) 2.3
4) none of the mentioned
-->"""))
        if a2==3:
            YourScore+=1
        else:
            print("Correct Answer=2.3")
        a3=int(input("""Which of the following is equivalent to random.randrange(3)?
1.range(3)
2.random.choice(range(0, 3))
3.random.shuffle(range(3))
4.random.select(range(3))
-->"""))
        if a3==2:
            YourScore+=1
        else:
            print("Correct Answer=2")
        a4=int(input("""The function random.randint(4) can return only one of the following values. Which?
1.4
2.3.4
3.error
4.5
-->"""))
        if a4==3:
            YourScore+=1
        else:
            print("Correct Answer=Error")
        a5=int(input("""Which of the following will not be returned by random.choice(“1 ,”)?
1) 1
2) (space)
3) ,
4) none of the mentioned
-->"""))
        if a5==4:
            YourScore+=1
        else:
            print("Correct Answer=None")
        a6=int(input("""Which of the following will never be displayed on executing print(random.choice({0: 1, 2: 3}))?
1) 0
2) 1
3) KeyError: 1
4) none of the mentioned
-->"""))
        if a6==1:
            YourScore+=1
        else:
            print("Correct Answer= 0")
        a7=int(input("""Which type of elements are accepted by random.shuffle()?
1) strings
2) lists
3) tuples
4) integers
-->"""))
        if a7==2:
            YourScore+=1
        else:
            print("Correct Answer=Lists")
        a8=int(input("""What is the range of values that random.random() can return?
1) [0.0, 1.0]
2) (0.0, 1.0]
3) (0.0, 1.0)
4) [0.0, 1.0)
-->"""))
        if a8==4:
            YourScore+=1
        else:
            print("correct Answer= 4")
    else:
        print("You Already completed this quiz")
def jav(a):  
    if "j" in a:
        global TotalScore,YourScore
        print("Welcome to Java quiz")
        TotalScore+=5
        a1=int(input("""Applets are __________ program.
1.Client Side
2.Server Side
3.Both 1 and 2
4.None of these
-->"""))
        if a1==1:
            YourScore+=1
        else:
            print("Correct Answer=1")
        a2=int(input("""2) Servlets are __________ program.
1.Client Side
2.Server Side
3.Both 1 and 2
4.None of these
-->"""))
        if a2==2:
            YourScore+=1
        else:
            print("Correct Answer=2")
        a3=int(input(""" What is JDBC?
1.It's a driver that is used for database connectivity in java.
2.It's a class that contains methods for Jar file development.
3.Both 1 and 2
4.None of these
-->"""))
        if a3==1:
            YourScore+=1
        else:
            print("Correct Answer=1")
        a4=int(input("""JDBC stands for __________.
1.Java Database Connection
2.Java Development Community
3.Java Development Code
4.Java Database Connectivity 
-->"""))
        if a4==4:
            YourScore+=1
        else:
            print("Correct Answer=4")
        a5=int(input(""" To use JDBC which of the following package is used?
1.java.jdbc
2.java.dbl
3.java.sql
4.java.net 
-->"""))
        if a5==3:
            YourScore+=1
        else:
            print("Correct Answer=3")

    else:
        print("You Already completed this quiz")

def cprog(a):
    global TotalScore,YourScore
    if "c" in a:
        print("Welcome to C/C++ quiz")
        TotalScore+=4
        a1=int(input("""main()\n{\nfloat me = 1.1;\ndouble you = 1.1;\nif(me==you)\nprintf("I love U");\nelse\nprintf(\"I hate U");\n}\n1.I Love U \n2.Error\n3.I hate U\n4.None\n-->"""))
        if a1==3:
            YourScore+=1
        else:
            print("Correct Answer=3.I hate U")
        a2=int(input("""#include <stdio.h>
void main(){
    unsigned char c=290;
    printf("%d",c);
}
1.Error
2.290
3.Garbage
4.34
-->"""))
        if a2==4:
            YourScore+=1
        else:
            print("Correct Answer=34")
        a3=int(input(""" 2. The operator used for dereferencing or indirection is ____
1.*
2.&
3.->
4. –>>
-->"""))
        if a3==1:
            YourScore+=1
        else:
            print("Correct Answer= *")
        a4=int(input(""" 5. Which of the following is illegal?
1.int *ip;
2.string s, *sp = 0;
3. int i; double* dp = &i;
4. int *pi = 0;
-->"""))
        if a4==3:
            YourScore+=1
        else:
            print("Correct Answer= c")
        a9=int(input(""" """))
        if a9==1:
            YourScore+=1
        else:
            print("Correct Answer=")
        a10=int(input("""Which one of the following is not a possible state for a pointer.
1) hold the address of the specific object
2) point one past the end of an object
3) zero
4) point to a type
-->"""))
        if a10==4:
            YourScore+=1
        else:
            print("Correct Answer=point to a type")
    else:
        print("You Already completed this quiz")

while 1:
    quiz()