import mysql.connector
import sys

def Connect():
    conn=None
    try:
        conn=mysql.connector.connect(
            host='148.163.122.62',
            port=86400,
            username='hancieph_user',
            password='Hienih@720**##2f',
            database='hancieph_hancie720'
        )
        print("Connected")

    except:
        print("Error", sys.exc_info())

    finally:

        return conn

Connect()
