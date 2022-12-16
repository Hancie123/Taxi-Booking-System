import mysql.connector
import sys

def Connect():
    conn=None
    try:
        conn=mysql.connector.connect(
            host='localhost',
            username='root',
            password='',
            database='level4b'
        )

    except:
        print("Error", sys.exc_info())

    finally:

        return conn

