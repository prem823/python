import mysql.connector

#create database connection
connection = mysql.connector.connect(host = "localhost" , username = "root" , password = "1a2b3c...," , database = "event")

# to check the connection is establish or not
if connection.is_connected():
    print("database is connected")
else:
    print("database is not connected")
    
# press 1 to add new event : eventname , eventdate , venue , eventid
# press 2 to get all event
# press 3 to delete event 
# press 4 to update event 
# press 5 to add student in event : studentname , stuemail , stumobile , studept , stuyear  , eventname
# press 6 to get all student
# press 7 to delete student
# press 8 to update student

eventdata = "create table if not exists eventdata(eventname text , eventdate text , venue text , eventid text)"
mycursor = connection.cursor()
mycursor.execute(eventdata)
connection.commit()
print("press 1 to add new event")
print("press 2 to get all event")
print("press 3 to delete event ")
print("press 4 to update event ")
print("press 5 to add student in event")
print("press 6 to get all student")
print("press 7 to delete student")
print("press 8 to update student")

select = int(input("enter no. 1 to 8 "))
# to add the new event
if(select==1):
    insertevent ="insert into eventdata values('{}' , '{}' , '{}' , '{}')".format(input("enter event name ") , input("enter event date ") , input("enter venue ") , int(input("enter eventid ")))
    mycursor.execute(insertevent)
    connection.commit()

# to get all events
elif(select==2):
    myevent = "select * from eventdata"
    mycursor.execute(myevent)
    print(mycursor.fetchall())
    connection.commit()
    
# to delete the event
elif(select==3):
    deletevent = "delete from eventdata where eventid ='1'"
    mycursor.execute(deletevent)
    connection.commit()

# to update the event
elif(select==4):
    updatevent = "update eventdata set eventname = 'NIGHT PARTY' , eventdate = '19.11.24' , venue = 'CHANAKYA AUDITORIUM' where eventid = '1'"
    mycursor.execute(updatevent)
    connection.commit()
        
studentdata = "create table if not exists studentdata(studname text , studemail text , studmobile text , studept text , studyear text , eventname text , studentid text)"
mycursor.execute(studentdata)
connection.commit()

# to add the student data
if(select==5):
    insertstudata = "insert into studentdata values('{}' , '{}' , '{}' , '{}' , '{}' , '{}' , '{}')".format(input("enter student name ") , input("enter student email ") , int(input("enter student mobile no.")) , input("enter student department name") , int(input("enter student year")) , input("enter event name ") , int(input("enter student id ")))
    mycursor.execute(insertstudata)
    connection.commit()    

# to get all student
elif(select==6):
    mystudata = "select * from studentdata"
    mycursor.execute(mystudata)
    print(mycursor.fetchall())
    connection.commit()

# to delete the student
elif(select==7):
    deletestudata = "delete from studentdata where studentid = '1'"
    mycursor.execute(deletestudata)
    connection.commit()

# to update the student data
elif(select==8):
    updatestudata  = "update studentdata set studyear = '3' where studentid = '1'"
    mycursor.execute(updatestudata)
    connection.commit()
    
elif(select>9):
    print("you have selected out of the range no.")