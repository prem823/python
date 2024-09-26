name="prem sharma"
age=19
gender="male"
email="prem0511.ps@gmail.com"
print(f"email is ={email}")
#data types in python 
print(type(name)) # type function return datatype of variable
print(type(age))
#1 str -> it can store the string data e.g. name ="prem sharma'
#2 int -> it can store the numeric data e.g. age =19
#3 float->it can store the decimal no e.g. percentge=75.45

#typecasting in python :- convert one datatype to another datatype
#e.g. sometimes when we purchse item in float we paid in integer
purchaseitemprice=90.32
paiditemprice=int(purchaseitemprice)
print("print amount is ",paiditemprice)
# note - string cant be converted into int reason string not ascii

#to get the input from the user using input ()function
collegename = input("enter your college name ")
collegefee=input("enter your collegefee")
print("my college name is "+collegename +" "+collegefee)
# note - the input function has default return type str 
# add scholarship of 25000 in fee
collegefees=int(collegefee)
collegefees = collegefees -25000
print("after my scholership fee ", collegefees)


                  