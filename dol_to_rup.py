# wap to convert the dollar into rupees and vice versa

choice = input("Enter your choice(d-r  or  r-d)= ")
if choice== "d-r":
    dollar = int(input("enter no. in dollars "))
    rupee = 84 * dollar
    print("no. in rupee" , rupee)
elif choice== "r-d":
    rupee = int(input("enter no. in rupees "))
    dollar = rupee / 84
    print("no. in dollars " , dollar)
else:
    print("your choice is wrong")