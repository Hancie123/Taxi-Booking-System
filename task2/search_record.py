from task2.libs import Libs
from task2.Driver_Management import searchRecord

email1=input("Enter email: ")
customer=searchRecord(email1)
if customer:
    print(customer)

else:
    print("Record not found")