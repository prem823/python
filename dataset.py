#list in python 
#list store multiple data
mylist= ["pawan","ivan","deepanshu"]

#tuple store multiple data
myset={"pawan","ivan","deepanshu"}
#dictionary store multiple data in key value pair
mydict={"name":"pawan","email":"p@gmail.com"}

#to check the  data  type of all above data
print("list:",type(mylist))
print("set:",type(myset),"dict:",type(mydict))

#how to identify list , set ,tuple, dictionary
#list-[],tuple-(),set-{},dict-{:}

#example of set data
myset={"pawan","deepanshu","mahi","pawam"}
mytuple=("pawan","deepanshu","mahi","pawam")
myclist=["pawan","deepanshu","mahi","pawam"]
mydict={"name":"pawan","age":33,"name":"pawan"}

#access  specific data from data set
print("list:",mylist[0])
print("tuple:", mytuple[0],"dict:",mydict["name"])

#access complete data form data set
for data in mylist:
    print(data)
for item in myset:
        print(item)
for value in mytuple:
            print("tuple",value)
for x in mydict.values():
        print("dict",x)

#to check which data set support duplicate data 
# list can contain the duplicate item
#set no duplicate item, it is unchangeable
#tuple can store duplicate item,it is unchangeable 
#dict no duplicate item
print("list",mylist,"tuple",mytuple,"dict",mydict,"set",myset)

#to update the data of all data set
myset[0]="tripti"
print(mylist)
mydict[0]="tripti"
print(mydict)
mytuple[0]="tripti"
print(mytuple)

mylist[0]="tripti"
print(mylist)

#tuple,set is unchangeable
#list , dict is changeable
#list, tuple duplicate item
#set, dict no duplicate itema                      

mylist.append("saloni")
myset.add("saloni")
mydict.update({"name":"saloni"})
print("list",mylist,"tuple",mytuple,"dict",mydict,"set",myset)

#to remove the data from data set
mydict.pop("name")
mylist.pop(0)
myset.remove("pawan")
print("list",mylist,"tuple",mytuple,"dict",mydict,"set",myset)

#convert tuple to list
convertlist =list(mytuple)
print(type(convertlist))
convertlist.append("rohan")
convertlist.pop(2)
print(convertlist)
mytuple=tuple(convertlist)
print(mytuple) 