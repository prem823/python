#error
#print(x)

#eror handling
try:
    print(x)
except NameError:
    print("'x' is not define")

#error 2
#   y=1/0
try:
    y=1/0
except ZeroDivisionError:
    print("divide by zero error")

#error 3 
name="prem"
#no = int(name)
try:
    no=int(name)
except ValueError:
    print("string cant convert into integer")

#error 4
friend =["ivan","anshu","wani"]
#friend[4] 
   
try:
    friend[4]
except IndexError:
    print("list out of rangle")    

#error 5
amount=500
email ="p@gmail.com"
#total =amount + email    
try:
    total = amount+ email
except TypeError:
    print("unsupported operand")