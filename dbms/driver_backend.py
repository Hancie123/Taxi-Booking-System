from dbms.connection import Connect
import sys
import mysql.connector


def driver_riding_total(did):
    conn=None
    sql="""select count(bookingid) from booking where did=%s"""
    values=(did,)
    result=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        result=cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return result


def driver_total_booked(did):
    conn=None
    sql="""select count(bookingid) from booking where did=%s and bookingstatus='Booked'"""
    values=(did,)
    result=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        result=cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return result

def driver_ridecompleted(did):
    conn=None
    sql="""select count(bookingid) from booking where did=%s and bookingstatus='Billing Completed'"""
    values=(did,)
    result=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        result=cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return result

def driver_ridecancelled(did):
    conn=None
    sql="""select count(bookingid) from booking where did=%s and bookingstatus='Incompleted'"""
    values=(did,)
    result=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        result=cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return result
