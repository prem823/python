# #object oriented programming structure
# #every thing is object

# #class-> it is a container which collection variables,functions
# #example-> tripti class
# # tripti.fullbane="triptisahu"
# # tripti.age=19
# # tripti.eating()
# # tripti.sleeping()
# # tripti.watching()
# # class syntaz
# class ClassName:
#    print("this  is my class")

class Prem:
    age=19
    fullname="Prem Sharma" 
    email="prem0511.ps@gmail.com"
    def pocketMoney(this,amount):            #function- pocketmoney     # object -amount
        print("my pocket money is",amount)
    def monthlySalary(this,daySalary):
        totalSalary=31* daySalary
        print("your monthly salaryis" , totalSalary)    

#object create class
prem:Prem=Prem()        
prem.pocketMoney(15000)
prem.monthlySalary(int(input("enter your one day salary")))
print(prem.fullname,prem.age,prem.email)




   