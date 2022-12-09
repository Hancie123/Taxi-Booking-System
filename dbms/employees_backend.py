import mysql.connector
import sys
from dbms.connection import Connect
from libs.employees_libs import EmployeesLibs


def insert_record(employeesInfo):
    conn=None
    sql="""INSERT INTO employees VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    values=(employeesInfo.getEmid(), employeesInfo.getName(), employeesInfo.getDob(), employeesInfo.getGender(),
            employeesInfo.getMobile(), employeesInfo.getEmail(), employeesInfo.getAddress())
    result=False
    try:
        conn=Connect()
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

def update_record(employeesInfo):
    conn=None
    sql="""UPDATE employees SET name=%s, dob=%s, gender=%s, mobile=%s, email=%s, address=%s WHERE emid=%s"""
    values=(employeesInfo.getName(), employeesInfo.getDob(), employeesInfo.getGender(),
            employeesInfo.getMobile(), employeesInfo.getEmail(), employeesInfo.getAddress(),employeesInfo.getEmid())
    updateResult=False
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql,values)
        conn.commit()
        cursor.close()
        conn.close()
        updateResult=True

    except:

        print("Error", sys.exc_info())

    finally:

        del sql
        del conn
        return updateResult
        return values


def search_employees(emid):
    conn=None
    sql="""SELECT * FROM employees WHERE emid=%s"""
    values=(emid,)
    employeesResult=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        employeesResult=cursor.fetchone()
        cursor.close()
        conn.close()


    except:
        print("Error", sys.exc_info())

    finally:
        del values, sql, conn
        return employeesResult

def delete_record(emid):
    conn=None
    sql="""DELETE FROM employees WHERE emid=%s"""
    values=(emid,)
    deleteResult=False

    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        deleteResult=True
    except:
        print("Error", sys.exc_info())

    finally:
        del values,sql,conn
        return deleteResult

def total_employees():
    conn=None
    sql="""SELECT count(emid) from employees"""
    employeesResult=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        employeesResult=cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return employeesResult

def select_allemployees():
    conn=None
    sql="""SELECT * FROM employees"""
    employeesResult=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        employeesResult=cursor.fetchall()
        cursor.close()
        conn.close()


    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return employeesResult


def search_employees111(name11):
    conn=None
    sql="""SELECT * FROM employees WHERE name LIKE '%{}%'""".format(name11)
    employeesResult=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        employeesResult=cursor.fetchall()
        cursor.close()
        conn.close()


    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return employeesResult



