import mysql.connector
import pandas as pd

cnx = mysql.connector.connect(user='root', password='**********************',
                              host='192.168.1.21',
                              database='employees')

mycursor = cnx.cursor()

dept_no_list = ['d001', 'd002', 'd003', 'd004', 'd005', 'd006', 'd007', 'd008', 'd009']

for i in dept_no_list:
    df = pd.read_sql(f"SELECT employees.*, departments.dept_name FROM departments INNER JOIN employees ON employees.dept_no = departments.dept_no where departments.dept_no = '{i}'", con=cnx)
    df.to_csv(f"{i}.csv", ",", "w")

for i in dept_no_list:
    data = pd.read_csv(f"{i}.csv")
    val1 = "INSERT INTO departments2 (dept_no, dept_name) VALUES (%s, %s)"
    val2 = (data.iloc[0].dept_no, data.iloc[0].dept_name)
    mycursor.execute(val1, val2)

cnx.close()