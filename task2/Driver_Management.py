import mysql.connector
import sys
from task2.Conn import connection
from task2.libs import Libs


def insert_record(recordInfo):
    conn=None
    sql="INSERT INTO customers VALUES (%s, %s, %s, %s, %s)"
    values=(recordInfo.getCid(), recordInfo.getName(), recordInfo.getDob(), recordInfo.getEmail(), recordInfo.getPassword())

    try:
        conn=connection()

        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        print("Inserted Successfully")

    except:
        print("The data inserted successfully")

    finally:
        del sql
        del conn

def searchRecord(email):
    conn=None
    sql="""SELECT * FROM customers WHERE email=%s"""
    values=(email,)
    customer=None
    try:
        conn=connection()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        customer=cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error", sys.exc_info())

    finally:
        del values
        del sql
        del conn
        return customer



def updateRecord(customerInfo):
    conn=None
    sql="UPDATE customers SET name=%s, dob=%s, email=%s, password=%s WHERE cid=%s"
    values=(customerInfo.getName(), customerInfo.getDob(), customerInfo.getEmail(), customerInfo.getPassword(), customerInfo.getCid())
    result=False
    try:
        conn=connection()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result=True

    except:
        print("Error", sys.exc_info())

    finally:
        del sql
        del conn
        del values
        return result
