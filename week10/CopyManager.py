import mysql.connector
import sys
import cusInfo

def connect():
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




def insert(cusInfo):
    conn=None
    sql="""INSERT INTO customers VALUES (%s, %s, %s, %s, %s)"""
    values=(cusInfo.getCid(), cusInfo.getName(), cusInfo.getDob(), cusInfo.getEmail(), cusInfo.getPassword())
    result={'status':False, 'message':None}

    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result['status']=True
        result['message']='Record save successfully'
        print("Inserted")

    except:
        result['status'] = False
        result['message'] = sys.exc_info()
        print("Error", sys.exc_info())

    finally:
        del values
        del sql
        return result


def getAll():
    pass

def search():
    pass

def edit():
    pass

def delete():
    pass