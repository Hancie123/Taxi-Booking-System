import mysql.connector
import sys

def insertRecord(record):
    conn=None
    sql="""UPDATE students SET name=%s, FCS=%s, ISD=%s WHERE sid=%s"""

    try:
        conn=mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='level4b'


 )
        cursor = conn.cursor()
        cursor.execute(sql, record)
        conn.commit()
        cursor.close()
        conn.close()
        print("Record updated")
    except:
        print("Error: ", sys.exc_info())
    finally:
        del sql
        del conn

record=['Hancie',99,99,1]
insertRecord(record)
