import sys
from cusInfo import Libs
import mysql.connector

def connect():
    conn = None
    try:
        conn = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='',
            database='level4b'
        )
    except:
        print("Error: ", sys.exc_info())
    finally:
        return conn

def insert(notebook):
    conn = None
    sql = """INSERT INTO notebooks VALUES(%s, %s, %s)"""
    values = (notebook.getNID(), notebook.getPages(), notebook.getPrice())
    result = False
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result =True
    except:
        print("Error: ", sys.exc_info())
    finally:
        del values
        del sql
        del conn
        return result




def search(cid):
    sql="""SELECT * FROM customers WHERE cid=%s"""
    record=None
    values=(cid,)
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        record=cursor.fetchone()  #return tuple
        cursor.close()
        conn.close()


    except:
        print("Error", sys.exc_info())

    finally:
        del sql
        return record
        return values



def edit(custInfo):
    conn = None
    sql = """UPDATE customers SET name=%s, dob=%s, email=%s,password=%s WHERE cid=%s"""
    values = (custInfo.getName(), custInfo.getDob(), custInfo.getEmail(), custInfo.getPassword(), custInfo.getCid())
    result = False
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result =True
    except:
        print("Error: ", sys.exc_info())
    finally:
        del values
        del sql
        del conn
        return result

def delete(cid):

        sql="""DELETE FROM customers WHERE cid=%s"""
        values=(cid, )
        result=False
        try:
            conn=connect()
            cursor=conn.cursor()
            cursor.execute(sql, values)
            conn.commit()
            cursor.close()
            conn.close()
            result=True

        except:
            print("Error", sys.exc_info())

        finally:
            del values, sql
            return result


def all():

    sql="""SELECT * from customers"""
    cust=None
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        cust=cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error", sys.exc_info())

    finally:
        del sql
        return cust
