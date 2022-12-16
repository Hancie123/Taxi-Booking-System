from Hancie.connection import Connect
from Hancie.libs import Libs
import mysql.connector
import sys

def insert_record(recordInfo):
    conn=None
    sql="""INSERT INTO customers VALUES (%s,(aes_encrypt(%s,'key')),%s,%s,%s)"""
    values=(recordInfo.getCid(),
            recordInfo.getName(),
            recordInfo.getDob(),
            recordInfo.getEmail(),
            recordInfo.getPassword())
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
        del values, sql, conn
        return result