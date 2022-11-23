import mysql.connector
import sys
from dbms.connection import connect
from libs.customer_libs import Customer_Libs


def insert_record(customerInfo):
    conn=None
    sql="""INSERT INTO customers VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    values=(customerInfo.getCid(), customerInfo.getName(), customerInfo.getDob(), customerInfo.getGender(),
            customerInfo.getMobile(), customerInfo.getEmail(), customerInfo.getAddress(), customerInfo.getPassword(), customerInfo.getCredit())
    result=False
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql,values)
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




