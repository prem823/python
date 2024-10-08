#file handling : work on file
#create file : syntax
#variablename=open("passward.txt","w")
#write fiile syntax
#eg
#mylaptoppassward=
#create file for saving my laptop passward
#open function will create  the file
#when file is not exits
mypassward=open("passward.txt","w")

#write my laptop passward in file
mypassward.write("my mackbook passward-guhiguhi")

#overwrite the new passward using userinput
mypassward.write(input("enter your new passward"))

#read the passward from file
mypassward=open("passward.txt","r")
print(mypassward.read())
if "laptop"==mypassward:
    print("yes")
else:
    print("no")``````````````