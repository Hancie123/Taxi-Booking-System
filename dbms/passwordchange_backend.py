import sys
from libs.customer_libs import Customer_Libs
from dbms.connection import Connect

def passwordChange(customerInfo):
    conn=None
    sql="""UPDATE customers SET password=%s WHERE cid=%s"""
    values=(customerInfo.getPassword(), customerInfo.getCid())
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
        print("Error", sys.exc_value)
    finally:
        del values,sql,conn
        return result