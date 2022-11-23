import sys

from task1.ManagerDriver import searchDriver
from task1.driver import Driver
from task2.Driver_Management import insert_record, searchRecord
from task2.libs import Libs


def manageCustomer():
    while(True):
        print("1. Add Customer")
        print("2. Search Customer")
        print("3. Edit Customer")
        print("4. Delete Customer")
        print("5. Display all Customer")
        print("0. Exit")
        cus = int(input("Enter your choice: "))

        if cus == 1:
            id = int(input("Enter ID: "))
            name = input("Enter name: ")
            dob = int(input("Enter DOB: "))
            email = input("Enter Email: ")
            password = input("Enter Password")

            d = Libs(id, name, dob, email, password)
            insert_record(d)

        elif cus == 2:

            email1 = input("Enter email: ")
            customer = searchRecord(email1)
            if customer:
                print(customer)

            else:
                print("Record not found")

        elif cus == 3:
            print("Customer Edited")
        elif cus == 4:
            print("Customer deleted")
        elif cus == 5:
            print("All Customer displayed")
        elif cus == 0:
            break


def manager():
    while (True):
        print("1. Add Manager")
        print("2. Search Manager")
        print("3. Edit Manager")
        print("4. Delete Manager")
        print("5. Display all Manager")
        print("0. Exit")
        man = int(input("Enter your choice: "))

        if man == 1:
            print("Manager added successfully")
        elif man == 2:
            lblno = input("Enter License No: ")
            d = Driver(licenseno=lblno)
            searchDriver(d)
        elif man == 3:
            print("Manager Edited")
        elif man == 4:
            print("Manager deleted")
        elif man == 5:
            print("All Manager displayed")
        elif man == 0:
            break

def trip():
    while (True):
        print("1. Add Trip")
        print("2. Search Trip")
        print("3. Edit Trip")
        print("4. Delete Trip")
        print("5. Display all Trip")
        print("0. Exit")
        trip = int(input("Enter your choice: "))

        if trip == 1:
            print("Trip added successfully")
        elif trip == 2:
            print("Trip Searched")
        elif trip == 3:
            print("Trip Edited")
        elif trip == 4:
            print("Trip deleted")
        elif trip == 5:
            print("All Trip displayed")
        elif trip == 0:
            break

while(True):

    print("----------------Main Menu-------------------")
    print("1. Customer Manager")
    print("2. Driver Manager")
    print("3. Trip Manager")
    print("0. Exit")
    print("-------------------------------")
    choice1=int(input("Enter your choice: "))
    print("-------------------------------")
    print("Choice is:" ,choice1)
    if choice1==0:
        print("Program exit")
        sys.exit()

    elif choice1==1:
        manageCustomer()


    elif choice1==2:
        manager()

    elif choice1==3:
        trip()

    else:
        print("Choice out of range")