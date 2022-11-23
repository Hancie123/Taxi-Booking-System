from task1.driver import Driver
from task1.ManagerDriver import searchDriver

lblno=input("Enter License No: ")
d=Driver(licenseno=lblno)
searchDriver(d)
