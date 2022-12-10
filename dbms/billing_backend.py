from dbms.connection import Connect
import sys
import mysql.connector


def billing_table():
    conn=None
    sql="""select customers.cid, booking.bookingid,drivers.did, customers.name,booking.date,
    booking.time, booking.pickupaddress, booking.dropoffaddress, drivers.name from booking
     left join customers on booking.cid=customers.cid left join drivers on 
     booking.bookingid=drivers.did where booking.bookingstatus='Bill Pending'"""
    result=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        result=cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return result