from task2.libs import Libs
from task2.Driver_Management import updateRecord

id=int(input("Enter ID: "))
name=input("Enter name: ")
dob=int(input("Enter DOB: "))
email=input("Enter Email: ")
password=input("Enter Password: " )

d=Libs(id, name, dob, email, password)
updateRecord(d)