import sys
from dbms.connection import Connect


def select_all720():
    conn=None
    sql="""SELECT distinct(bookingid) FROM booking"""
    Bookresult=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        Bookresult=cursor.fetchall()
        cursor.close()
        conn.close()


    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return Bookresult