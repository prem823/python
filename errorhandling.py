#error handling or execution handling
#control over the error in program

#error in program
#print(x)

#solution
try:
    print(x)
except NameError:
    print("x is not defined")  

#error type in python 
x="prem"
y = 5
c = x + y
print(c)      