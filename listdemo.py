# list can store multiple data , data can be different types like- int ,string, float
# list can float the duplicate data
#list is an ordered data set-sorting ascending decending

#create list and store your friends name
friendlist=["ivaan","anshu","anjali","wani"]
# print the list of class names
print(friendlist)

#add the age of your friend into list
# append will add the data into end of the list 
friendlist.append(36)
friendlist.append(26)
friendlist.append(29)
friendlist.append(5)
print(friendlist)
 
 #add the data into list using index no
friendlist.insert(3,"prem")
print(friendlist)

#to access the data using index no
print(friendlist[2])
print(friendlist[3])

#access the complete list
for name in friendlist:
    print(name)

#to  delete the data form list 
#remove will delete the data using value
friendlist.remove("prem")
print(friendlist)

#pop will delete the data using index
friendlist.pop(1)
print(friendlist)

#add the 5  favt city name in list
#add my favt city kasol in first index
#remove the last city in list
#print the list data

factcity=["ghaziabad","gungaon","goa","jaipur"]
factcity.insert(0,"kasol")
factcity.pop(4)
factcity .sort()
print(factcity)