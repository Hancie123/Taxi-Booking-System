import mysql.connector
import sys
from dbms.connection import Connect
from libs.customer_libs import Customer_Libs


def insert_record(customerInfo):
    conn=None
    sql="""INSERT INTO customers VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s, %s)"""
    values=(customerInfo.getCid(), customerInfo.getName(), customerInfo.getDob(), customerInfo.getGender(),
            customerInfo.getMobile(), customerInfo.getEmail(), customerInfo.getAddress(), customerInfo.getPassword(), customerInfo.getCredit(), customerInfo.getStatus())
    result=False
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql,values)
        conn.commit()
        cursor.close()
        conn.close()
        result=True

    except:

        print("Error", sys.exc_info())

    finally:

        del sql
        del conn
        return result
        return values

def update_record(customerInfo):
    conn=None
    sql="""UPDATE customers SET name=%s, dob=%s, gender=%s, mobile=%s, email=%s, address=%s,credit=%s, status=%s WHERE cid=%s"""
    values=(customerInfo.getName(), customerInfo.getDob(), customerInfo.getGender(),
            customerInfo.getMobile(), customerInfo.getEmail(), customerInfo.getAddress(),customerInfo.getCredit(), customerInfo.getStatus(), customerInfo.getCid())
    updateResult=False
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql,values)
        conn.commit()
        cursor.close()
        conn.close()
        updateResult=True

    except:

        print("Error", sys.exc_info())

    finally:

        del sql
        del conn
        return updateResult
        return values


def search_customer(cid):
    conn=None
    sql="""SELECT *, old_password(password) as Pw FROM customers WHERE cid=%s"""
    values=(cid,)
    customerResult=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        customerResult=cursor.fetchone()
        cursor.close()
        conn.close()


    except:
        print("Error", sys.exc_info())

    finally:
        del values, sql, conn
        return customerResult

def delete_record(cid):
    conn=None
    sql="""DELETE FROM customers WHERE cid=%s"""
    values=(cid,)
    deleteResult=False

    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        deleteResult=True
    except:
        print("Error", sys.exc_info())

    finally:
        del values,sql,conn
        return deleteResult

def search_customer2(name12):
    conn=None
    sql="""SELECT * FROM customers WHERE name LIKE '%{}%'""".format(name12)

    customerResult=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        customerResult=cursor.fetchall()
        cursor.close()
        conn.close()


    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return customerResult


def update_customer_record(customerInfo):
    conn=None
    sql="""UPDATE customers SET name=%s, dob=%s, gender=%s, mobile=%s, email=%s, address=%s,credit=%s WHERE cid=%s"""
    values=(customerInfo.getName(), customerInfo.getDob(), customerInfo.getGender(),customerInfo.getMobile(), customerInfo.getEmail(), customerInfo.getAddress(),customerInfo.getCredit(), customerInfo.getCid())
    updateResult=False
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql,values)
        conn.commit()
        cursor.close()
        conn.close()
        updateResult=True

    except:

        print("Error", sys.exc_info())

    finally:

        del sql
        del conn
        return updateResult
        return values



