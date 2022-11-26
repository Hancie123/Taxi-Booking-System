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