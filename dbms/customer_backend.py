import sys
from dbms.connection import Connect
from libs.customer_libs import Customer_Libs



def total_customer():
    conn=None
    sql="""SELECT count(cid) from customers"""
    result=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        result=cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return result


def select_allcustomer():
    conn=None
    sql="""SELECT * from customers"""
    result=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        result=cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return result


def validaecustomerbooking(cid):
    conn=None
    sql="""select date from booking where cid=%s and bookingstatus='Pending'"""
    values=(cid,)
    validateresult=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql,values)
        validateresult=cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return validateresult
