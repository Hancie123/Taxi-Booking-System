import mysql.connector
import sys

def insertRecord(record):
    conn=None
    sql="""INSERT INTO students VALUES (%s, %s, %s, %s)"""

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
        print("Data inserted successfully")
    except:
        print("Error: ", sys.exc_info())
    finally:
        del sql
        del conn

record=[1,'Hancie Phago',98,99]
insertRecord(record)
