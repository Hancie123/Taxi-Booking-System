from task2.libs import Libs
from task2.Driver_Management import updateRecord, searchRecord

email=input("Enter Email: ")
customer=searchRecord(email)
if len(customer)==0:
    print("Record not found")
else:
    print(customer)
    id = int(input("Enter ID: "))
    name = input("Enter name: ")
    dob = int(input("Enter DOB: "))
    email = input("Enter Email: ")
    password = input("Enter Password")
    d = Libs(id, name, dob, email, password)
    result=updateRecord(d)
    if result==True:
        print("Record Updated")

    else:
        print("Record not updated")
