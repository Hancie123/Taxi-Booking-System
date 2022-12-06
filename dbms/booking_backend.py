from libs.booking_libs import BookingLibs
from dbms.connection import Connect
import sys

def insert_booking(bookingInfo):
    conn=None
    sql="""INSERT INTO booking VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
    values=(bookingInfo.getBookingid(), bookingInfo.getPickupaddress(), bookingInfo.getDate(),
            bookingInfo.getTime(), bookingInfo.getDropoffaddress(), bookingInfo.getBookingstatus(),
            bookingInfo.getCid(), bookingInfo.getDid())
    insertResult=False

    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        insertResult=True

    except:
        print("Error",sys.exc_info())

    finally:
        del values, sql, conn
        return insertResult

#
# def select_all(cid):
#     conn=None
#     sql="""SELECT * FROM booking WHERE cid=%s"""
#     values=(cid,)
#     Bookresult=None
#     try:
#         conn=Connect()
#         cursor=conn.cursor()
#         cursor.execute(sql, values)
#         Bookresult=cursor.fetchall()
#         cursor.close()
#         conn.close()
#
#
#     except:
#         print("Error", sys.exc_info())
#
#     finally:
#         del values, sql, conn
#         return Bookresult


def total_booking():
    conn=None
    sql="""SELECT count(bookingid) from booking"""
    bookingResult=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        bookingResult=cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return bookingResult