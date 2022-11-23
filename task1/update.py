from task1.driver import Driver
from task1.ManagerDriver import updateDriver

did=int(input("Enter ID: "))
name=input("Enter name: ")
lblno=input("Enter License: ")

d1=Driver(did, name, lblno)
updateDriver(d1)