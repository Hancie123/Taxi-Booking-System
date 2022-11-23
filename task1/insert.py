from task1.driver import Driver
from ManagerDriver import saveDriver

#Test1
# d1=Driver()
# d1.setDid(1)
# d1.setName('Hancie Phago')
# d1.setLicenseno('BS1002720')
# saveDriver(d1)


#Test2

did=name=lno=None

did=int(input("Enter ID: "))
name=input("Name: ")
lno=input("License No: ")

d2=Driver(did, name, lno)
saveDriver(d2)
