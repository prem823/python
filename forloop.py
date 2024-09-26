#forloop is uesd foor no. of iteration

username="prem sharma"
for x in username:
    print(x)

    #print 1 to 10 using for loop
for i in range(1,11):
    print(i)


#wap  to create table of any two
tableno= int(input("enter the no="))
for a in range(1,11):
    print(tableno* a) 

#wap to print even no 1 to 10

for b in range(1,11):
    if b%2  ==0:
       print(b)

#wap print this pattern 1 4 7 10 13 using for loop

for c in range(1,14,3):
    print(c)

#wap print this parttern 1 3 7 11 13 15 using for
for b in range (1,16,2):
    if b== 9 or b==5:
        continue # skip the current iteration 
    else :   
        print(b)


