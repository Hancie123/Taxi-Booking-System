from libs.myactivity_libs import MyActivity
from dbms.connection import Connect
import sys

def activity_insert(activityInfo):
    conn=None
    sql="""INSERT INTO myactivity values (%s, %s, %s, %s, %s, %s, %s, %s)"""
    values=(activityInfo.getMyid(), activityInfo.getSystem(), activityInfo.getModel(),
            activityInfo.getMachine(), activityInfo.getProcessor(), activityInfo.getDate(),
            activityInfo.getDate2(), activityInfo.getCid())
    activityResult=False
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()



    except:
        print("Error", sys.exc_info())

    finally:
        del values,sql,conn
        return activityResult
