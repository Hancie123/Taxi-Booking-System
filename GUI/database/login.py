import mysql.connector
import sys

from GUI.database import Global


def userLogin(userInfo):
    conn=None
    sql=None

    try:

        sql = "SELECT * FROM user WHERE email=%s and password=%s"
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='level4b'

        )

        cursor = conn.cursor()
        cursor.execute(sql, userInfo)
        user = cursor.fetchone()
        if user == None:
            print("User not found")

        else:
            print("Welcome ", user[1])
            Global.currentUser=user
        cursor.close()
        conn.close()

    except:
        print("Error", sys.exc_info()[0])

    finally:
        del sql
        del conn

userInfo = ['raj@gmail.com', '123']
userLogin(userInfo)


