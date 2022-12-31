from libs.driver_libs import Driver_Libs
from dbms.connection import Connect
import sys


def customer_driver_history(cid):
    conn=None
    sql="""select booking.did,drivers.name, booking.date, booking.time, booking.pickupaddress, 
    booking.dropoffaddress, drivers.mobile from customers 
    inner join booking on customers.cid=booking.cid inner join drivers
on booking.did=drivers.did where customers.cid=%s order by booking.bookingid desc;"""
    values=(cid,)
    historyResult=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        historyResult=cursor.fetchall()


    except:
        print("Error", sys.exc_info())

    finally:
        del values, sql, conn
        return historyResult