from libs.driver_libs import Driver_Libs
from dbms.connection import Connect
import mysql.connector
import sys

def insert_record(driverInfo):
    conn=None
    sql="""INSERT INTO `drivers`VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    values=(driverInfo.getDid(), driverInfo.getName(), driverInfo.getMobile(), driverInfo.getEmail(),
            driverInfo.getLicense(), driverInfo.getPassword(),driverInfo.getDriverstatus())
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
        del sql
        del conn
        return result
        return values

def search_record(did):
    conn=None
    sql="""SELECT *, old_password(password) as Pw FROM drivers WHERE did=%s"""
    values=(did,)
    searchResult=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        searchResult=cursor.fetchone()
        cursor.close()
        conn.close()

    except:
        print("Error", sys.exc_info())
    finally:
        del values, sql, conn
        return searchResult

def delete_record(did):
    conn=None
    sql="""DELETE FROM drivers WHERE did=%s"""
    values=(did,)
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

        del values, sql,conn
        return result

def update_record(driverInfo):
    conn=None
    sql="""UPDATE drivers SET name=%s, mobile=%s, email=%s, license=%s WHERE did=%s"""
    values=(driverInfo.getName(), driverInfo.getMobile(), driverInfo.getEmail(), driverInfo.getLicense(), driverInfo.getDid())
    updateresult=False
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        updateresult=True

    except:
        print("Error", sys.exc_info())

    finally:
        del values, sql, conn
        return updateresult

def update_DriverStatus(driverInfo):
    conn=None
    sql="""UPDATE drivers SET driverstatus=%s WHERE did=%s"""
    values=(driverInfo.getDriverstatus(),driverInfo.getDid())
    updateresult=False
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        updateresult=True

    except:
        print("Error", sys.exc_info())

    finally:
        del values, sql, conn
        return updateresult

def driver_select_all(driverID):
    conn=None
    sql="""SELECT * FROM drivers WHERE did=%s"""
    values=(driverID,)
    selectResult=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        selectResult=cursor.fetchone()
        cursor.close()
        conn.close()


    except:
        print("Error", sys.exc_info())

    finally:
        del values, sql, conn
        return selectResult


def total_driver():
    conn=None
    sql="""SELECT count(did) from drivers"""
    driverResult=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        driverResult=cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return driverResult

def available_driver():
    conn=None
    sql="SELECT * FROM drivers WHERE driverstatus='Active'"
    availableDriver=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        availableDriver=cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return availableDriver

def select_alldriver():
    conn=None
    sql="SELECT * FROM drivers"
    availableDriver=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        availableDriver=cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return availableDriver

def driver_selectallbooking(did):
    conn=None
    sql="""select booking.bookingid, booking.pickupaddress, booking.date, booking.time, booking.dropoffaddress,
     customers.name, booking.bookingstatus from booking inner join customers
      on booking.cid=customers.cid where booking.did=%s and booking.bookingstatus='Booked'"""
    values=(did,)
    driverResult=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        driverResult=cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return driverResult

def driver_select_all22(name11):
    conn=None
    sql="""SELECT * FROM drivers WHERE name LIKE '%{}%'""".format(name11)

    selectResult=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        selectResult=cursor.fetchall()
        cursor.close()
        conn.close()


    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return selectResult

def driver_trip_history(did):
    conn=None
    sql="""select customers.cid, customers.name, booking.date, booking.time, 
    booking.pickupaddress, booking.dropoffaddress from booking inner join customers
     on booking.cid=customers.cid where booking.did=%s and booking.bookingstatus='Billing Completed'"""
    values=(did,)
    driverResult=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        driverResult=cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return driverResult

def driver_password_change(Driver):
    conn=None
    sql="""UPDATE drivers SET password=%s WHERE did=%s"""
    values=(Driver.getPassword(), Driver.getDid())
    changepasswordresult=False

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        changepasswordresult = True
    except:
        print("Error", sys.exc_info())
    finally:
        del values, sql,conn
        return changepasswordresult


