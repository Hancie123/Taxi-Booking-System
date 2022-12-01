from libs.driver_libs import Driver_Libs
from dbms.connection import Connect
import mysql.connector
import sys

def insert_record(driverInfo):
    conn=None
    sql="""INSERT INTO `drivers`VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
    values=(driverInfo.getDid(), driverInfo.getName(), driverInfo.getMobile(), driverInfo.getEmail(),
            driverInfo.getLicense(), driverInfo.getPassword(),driverInfo.getStatus(), driverInfo.getDriverstatus())
    result=False
    try:
        conn=Connect()
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
        return result
        return values

def search_record(did):
    conn=None
    sql="""SELECT * FROM drivers WHERE did=%s"""
    values=(did,)
    searchResult=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        searchResult=cursor.fetchone()
        cursor.close()
        conn.close()

    except:
        print("Error", sys.exc_info())
    finally:
        del values, sql, conn
        return searchResult

def delete_record(did):
    conn=None
    sql="""DELETE FROM drivers WHERE did=%s"""
    values=(did,)
    result=False
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result=True

    except:
        print("Error", sys.exc_info())

    finally:

        del values, sql,conn
        return result

def update_record(driverInfo):
    conn=None
    sql="""UPDATE drivers SET name=%s, mobile=%s, email=%s, license=%s, password=%s WHERE did=%s"""
    values=(driverInfo.getName(), driverInfo.getMobile(), driverInfo.getEmail(), driverInfo.getLicense(), driverInfo.getPassword(), driverInfo.getDid())
    updateresult=False
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        updateresult=True

    except:
        print("Error", sys.exc_info())

    finally:
        del values, sql, conn
        return updateresult




