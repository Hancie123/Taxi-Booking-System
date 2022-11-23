import mysql.connector
import sys

def connection():
    conn=None
    try:

        conn=mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='level4b'
        )


    except:

        print("Error", sys.exc_info())



    finally:
        return conn

connection()

