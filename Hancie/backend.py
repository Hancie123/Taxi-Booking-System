import connection
import mysql.connector
import sys

def insert_record(recordInfo):
    conn=None
    sql="""INSERT INTO customers VALUES (%s,%s,%s,%s,%s)"""
    values=(recordInfo.getCid(), recordInfo.getName(), recordInfo.getDob(), recordInfo.getEmail(), recordInfo.getPassword() )
    try:
        pass

    except:
        pass

    finally:
        pass