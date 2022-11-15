import mysql.connector
import sys

from GUI.oop.gui import book1


def saveBook(bookInfo):
    conn=None
    values=(bookInfo.getBID(),bookInfo.getTitle(), bookInfo.getWriter(), bookInfo.getPublished(), bookInfo.getPrice())
    sql="""INSERT INTO book VALUES (%s, %s, %s, %s,%s)"""

    try:
        conn=mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='',
            database='level4b'

        )
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        print("Book saved")

    except:
        print("Error: ", sys.exc_info())

    finally:
        del sql
        del conn


saveBook(book1)








