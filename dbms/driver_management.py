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


