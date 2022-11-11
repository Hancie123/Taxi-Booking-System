import mysql.connector
import sys

def deleteRecord(sid):
    conn=None
    sql="""DELETE FROM students WHERE sid=%s"""
    values=[sid]

    try:
        conn=mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='level4b'


 )
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        print("Record deleted")
    except:
        print("Error: ", sys.exc_info())
    finally:
        del sql
        del conn


deleteRecord(1)
