#conditional statement will check the condition is true or not
# #to check the condition statement we use if else

#WAP to check user eligible for voting 
userage= int(input("enter your age"))
#note the default input function return
# for vote userage must be greater than 18
if userage > 18:
    print("you are eligible for voting")
else:
    print("you are not eligible for voting")

#wap to check user can sit in compartment in metro
gender=input("enter your gender")
if gender== "male":
   print("you are  not allowed in  compartment")
elif gender=="female": 
    print("you are allowed to sit in  compartment")
else:

    print("you can sit in compartment")
   

   #wap if gender is female and age greater than 18 - govt job apply else male age is greater than 18 - private job apply

if gender=="female" and userage>18 :
    print("you are eligible for govt job")
elif  gender =="male" and userage>18:
    print("you are eligible for private job")
else: 
    print("you are not eligible")  
    