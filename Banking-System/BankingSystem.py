# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 13:10:56 2020

@author: Achyuth
"""

custName = ['Achyuth KP', 'Manoj A', 'Sai Pavan', 'Suraj Lokesh', 'Nithin BR']
custPin = ['0123', '2575', '7275', '2312', '5049']
custBalance = [900000, 20000, 20000, 40000, 10000]

# This statement below helps the program to run continuously.
while True:
    print("-"*37)
    print(" ----Welcome to Achu's Bank----       ")
    print("*"*37)
    print("=<< 1. Open a new account         >>=")
    print("=<< 2. Withdraw Money             >>=")
    print("=<< 3. Deposit Money              >>=")
    print("=<< 4. Check your details         >>=")
    print("=<< 5. Exit/Quit                  >>=")
    print("*"*37)
    # The below statement takes the choice number from the user.
    choice = int(input("Select your choice number from the above menu : "))
    if choice == 1:
        print("Thanks Choosing our Bank\nKindly fill the required Bank details\n")
        name=input("Enter your FullName-->")
        pin=int(input("Create a pin to access your account in future->"))
        Bal=int(input('Please add some money into your account'))
        custName.append(name)
        custPin.append(pin)
        while Bal<100:
            print("Add money more than Rs.100")
            Bal=int(input('Please add some money into your account-->'))
        print("----New account created successfully !----\n")
        print("Note! Please remember the Name and Pin")
        print("="*37)
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choice==2:
        pin=input("Enter your pin")
        for i in range(len(custPin)):
            if pin==custPin[i]:
                print("Your Current Balance-->",custBalance[i])
                withdraw=int(input("Enter the amount you want to withdraw"))
                while withdraw<custBalance[i]:
                    print("Your Current Balance-->",custBalance[i])
                    withdraw=int(input("Enter the amount you want to withdraw"))
                custBalance-=withdraw    
                print(f"Amount {withdraw} as been debited from our account")
                print("----Withdraw Successful!----")
                print("Your Current Balance-->",custBalance[i])
            else:
                print("Your name and pin does not match!\n")
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choice==3:
        pin=input("Enter your pin")
        for i in range(len(custPin)):
            if pin==custPin[i]:
                print("Your Current Balance-->",custBalance[i])
                dep=int(input("Enter the amout you want to Deposit"))
                custBalance+=dep
                print("Your Current Balance-->",custBalance[i])
                print("----Deposition successful!----")                
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choice==4:
         pin=int(input("Enter your current pin"))
         for i in range(len(custPin)):
             if pin==custPin[i]:
                 print("Your name-->{}\nYour Current Balance-->{}\n")
         mainMenu = input("Please press enter key to go back to main menu to perform another fuction or exit ...")
    elif choice == 5:
        # These statements would be just showed to the customer.
         print("Choice number 5 is selected by the customer")
         print("Thank you for using our banking system!")
         print("\n")
         print("Come again")
         print("Bye bye")
         break
    else:
        # This else function above would work when a wrong function is chosen.
         print("Invalid option selected by the customer")
         print("Please Try again!")
        # This statement below helps the user to go back to the start of the program (main menu).
         mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")