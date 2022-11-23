import mysql.connector
import sys

def connect():
    conn=None
    try:
        conn=mysql.connector.connect(
            host='localhost',
            username='root',
            password='',
            database='taxi_booking_system'
        )

    except:
        print("Error", sys.exc_info())

    finally:

        return conn

