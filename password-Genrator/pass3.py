# Password Generator
# written by Achyuth
import string
import random

def GeneratePassword(passLength):
    password = string.ascii_letters + string.digits + "!@#$%^&*()_+=-./?><|\}{[]"
    # generating characters, numbers and letters for password
    passwordList = []
    # password list is for putting all the selected password units into a string and show them to user
    for passChar in range(passLength):
        passRandom = random.choice(password)
        passwordList.append(passRandom)

    finalOutput = "".join(passwordList)
    return finalOutput


while 1:
    userPasswordLength = int(input("Enter Length For Your Password: \n"))
    print(GeneratePassword(userPasswordLength))
    userReply = input("Do You Want More? (y,n): ")
    if userReply.lower() == "y":
        continue
    elif userReply.lower() == "n":
        break
