import mysql.connector
import sys

def searchrecord(sid):
    conn=None
    sql="""SELECT * FROM students WHERE sid=%s"""
    values=[sid,]

    try:
        conn=mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='level4b'


 )
        cursor = conn.cursor()
        cursor.execute(sql, values)
        record=cursor.fetchone()
        if record:
            print(record)
            print("record found")

        else:
            print("record not found")

        cursor.close()
        conn.close()


    except:
        print("Error: ", sys.exc_info())
    finally:
        del sql
        del conn


searchrecord(1)
