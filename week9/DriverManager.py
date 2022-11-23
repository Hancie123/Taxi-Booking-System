import mysql.connector
import sys
from task1.driver import Driver

def connect():
    conn=None
    try:
        conn = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='',
            database='level4b'
        )
    except:
        print("Error", sys.exc_info())
    finally:
        return conn


def saveDriver(driverInfo):
    conn=None
    sql="""INSERT INTO drivers VALUES (%s, %s, %s)"""
    values=(driverInfo.getDid(), driverInfo.getName(), driverInfo.getLicenseno())
    try:
        conn=mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='',
            database='level4b'
        )
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        print("Save driver record")

    except:
        print("Error", sys.exc_info())

    finally:
        del values
        del sql
        del conn



def searchDriver(licenseno):

    conn=None
    sql="""SELECT * FROM drivers WHERE licenseno=%s"""
    values=[licenseno.getLicenseno()]
    driver=None
    try:
        conn=mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='level4b'
        )
        cursor=conn.cursor()
        cursor.execute(sql, values)
        driver=cursor.fetchall()
        if driver:
            print(driver)
        else:
            print("Not found")

    except:

        print("Error", sys.exc_info())

    finally:
        del sql
        del conn
        return driver

def updateDriver(driverInfo):
    conn=None
    sql="""UPDATE drivers SET name=%s, licenseno=%s WHERE did=%s"""
    values=(driverInfo.getName(), driverInfo.getLicenseno(), driverInfo.getDid())

    try:
        conn=mysql.connector.connect(
            host="localhost",
            user='root',
            password='',
            database='level4b'
        )

        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        print("Updated Driver Info")
    except:
        print("Error: ", sys.exc_info())
    finally:
        del values
        del sql
        del conn


def deleteDriver(did):

    conn=None
    sql="""DELETE FROM drivers WHERE did=%s"""
    values=[did.getDid()]
    try:
        conn=mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='level4b'
        )

        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        print("Data deleted successfully")
    except:
        print("Error", sys.exc_info())
    finally:
        del values
        del sql
        del conn

def allDriver(did):
    conn=None
    sql="""SELECT * FROM drivers WHERE did=%s"""
    values=[did.getDid()]

    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        record=cursor.fetchone()
        print(record)
        cursor.close()
        conn.close()
    except:

        print("Error", sys.exc_info())
    finally:
        del sql
        del conn

