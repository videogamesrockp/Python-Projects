import mysql.connector
import json
from employee import employee
from department import department
import jsonpickle
import os

cnx = mysql.connector.connect(user='root', password='******************',
                              host='192.168.1.21',
                              database='employees')
os.chdir("*************")

mycursor = cnx.cursor()

mycursor.execute("select emp_no, first_name, last_name from employees where dept_no = 'd001'")
results = mycursor.fetchall()
dept1 = department("d001", "Marketing", [])


for  i in results:
    e = employee(i[0], i[1], i[2])
    dept1.emp_list.append(e)


with open("main.json", "w") as f:
    deptJSON = jsonpickle.encode(dept1, unpicklable=False)
    deptJSON = jsonpickle.decode(deptJSON)
    json.dump(deptJSON, f, indent=4, separators=(", ", ": "), sort_keys=True, default=str)