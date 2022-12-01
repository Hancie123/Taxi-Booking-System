from libs.customer_libs import Customer_Libs
from dbms.connection import Connect
import mysql.connector
import sys

def login(loginInfo):
    conn=None
    sql="SELECT * FROM customers WHERE email=%s and password=%s"
    values=(loginInfo.getEmail(), loginInfo.getPassword())
    user=None

    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        user = cursor.fetchone()
        cursor.close()
        conn.close()


    except:
        print("Error", sys.exc_info())

    finally:
        del sql
        del conn
        return user
        return values

def driverlogin(driverInfo):

    sql="""SELECT * FROM drivers WHERE email=%s and password=%s"""
    values=(driverInfo.getEmail(), driverInfo.getPassword())
    driverresult=None

    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        driverresult=cursor.fetchone()
        cursor.close()
        conn.close()

    except:
        print("Error", sys.exc_info())

    finally:
        del values, sql
        return driverresult

def adminLogin(adminInfo):

    sql="""SELECT * FROM admin WHERE email=%s and password=%s"""
    values=(adminInfo.getEmail(), adminInfo.getPassword())
    adminresult=None

    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        adminresult=cursor.fetchone()
        cursor.close()
        conn.close()

    except:
        print("Error", sys.exc_info())

    finally:
        del values, sql
        return adminresult