from task1.driver import Driver
from task1.ManagerDriver import deleteDriver

did1=int(input("Enter ID: "))
d1=Driver(did1)
deleteDriver(d1)