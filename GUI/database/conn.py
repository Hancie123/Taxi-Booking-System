import sys
import mysql.connector


def connectdb():
    conn = None
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='level4b'
        )
        conn.close()
        print("The database is connected successfully")
    except:

        print("Error: ", sys.exc_info())

    finally:
        # remove all the used resources(variables, files, database, netword)
        del conn

connectdb()


#Insert Record
def insertrecord():
    conn=None
    sql="INSERT INTO person VALUES (2,'Ajaya','KTM')"
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='level4b'
        )
        curser=conn.cursor()
        curser.execute(sql)
        conn.commit()
        curser.close()
        conn.close()
        print("Insert record successfully")
    except:
        print("Error: ", sys.exc_info())
    finally:
        del sql
        del conn

insertrecord()



#Insert Record
def updaterecord():
    conn=None
    sql="UPDATE person SET Name='Nitesh' WHERE ID=2"
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='level4b'
        )
        curser=conn.cursor()
        curser.execute(sql)
        conn.commit()
        curser.close()
        conn.close()
        print("Update record successfully")
    except:
        print("Error: ", sys.exc_info())
    finally:
        del sql
        del conn



updaterecord()


def selectall():
    conn = None
    sql = "SELECT * FROM person"
    try:
        conn = mysql.connector.connect(

            host="localhost",
            user="root",
            password="",
            database="level4b"
            )
        cursor = conn.cursor()
        cursor.execute(sql)
        result=cursor.fetchall()
        for x in result:
            print(x)
        cursor.close()
        conn.close()
    except:

       print("Error: ", sys.exc_info())

    finally:
        del conn
        del sql


selectall()