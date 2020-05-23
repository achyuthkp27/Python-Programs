#This is my first python program i did on my own

#This program will extract all the city names and mail_id's from an input file and displays all the city names present in the file

f=open("file1.txt","r")
if f.mode=="r":
    #This will display the content present in the file1
    print("Data present in the file is:\n")
    print(f.read())
    print("\n")

f=open("file1.txt","r")
#This will split each word present in the file
#Individual words will be assigned to variable content as list
content=f.read().split()
content_len=len(content) #This will get the length of the content list
   
#Now we need to open the file,which contains all the known city names
city_list=list()
city_count=0
y=open("file2.txt", "r")
city_names = y.read().split()
for n in range(content_len):
    if content[n].lower() in city_names:
        if not content[n].upper() in city_list:
            city_list.append(content[n].upper())
            city_count+=1
#Display all the city names present
print("I found {} city names in the given input file\n{}".format(city_count,city_list))

a="@gmail.com"
o=len(a)
mails=[]
for n in range(content_len):
    i=len(content[n])
    if content[n][i-o:i+1:] == a:
        mails.append(content[n])
print(mails)