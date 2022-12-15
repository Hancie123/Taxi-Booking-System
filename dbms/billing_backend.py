from dbms.connection import Connect
import sys
import mysql.connector


def insert_billing(billingID):
    conn=None
    sql="""INSERT INTO billing VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    values=(billingID.getBillingid(), billingID.getName(), billingID.getKm(),
            billingID.getUnit(), billingID.getTotal(), billingID.getBookingid(), billingID.getDate())
    result=False

    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result=True

    except:
        print("Error", sys.exc_info())

    finally:
        del values, sql, conn
        return result


def billing_table():
    conn=None
    sql="""select customers.cid, booking.bookingid,drivers.did, customers.name,customers.credit, booking.date,
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

def billing_history12():
    conn=None
    sql="""select booking.bookingid, billing.name,booking.pickupaddress, 
    booking.dropoffaddress,booking.date, booking.time, billing.km, 
    billing.unit, billing.total from booking left join billing on 
    booking.bookingid=billing.bookingid left join customers on 
    booking.cid=customers.cid where booking.bookingstatus='Billing Completed'"""
    billingResult=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        billingResult=cursor.fetchall()
        cursor.close()
        conn.close()


    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return billingResult

def customer_billing_history(custInfo):
    conn=None
    sql="""select booking.pickupaddress, booking.dropoffaddress, booking.date,booking.time,
     billing.km, billing.unit, billing.total from booking inner join 
     billing on booking.bookingid=billing.bookingid where booking.cid=%s"""
    values=(custInfo,)
    billingHistory=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql,values)
        billingHistory=cursor.fetchall()
        cursor.close()
        conn.close()


    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return billingHistory