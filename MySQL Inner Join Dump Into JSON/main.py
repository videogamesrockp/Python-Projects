import json
import mysql.connector


cnx = mysql.connector.connect(user='root', password='***********',
                              host='192.168.1.21',
                              database='employees')

mycursor = cnx.cursor()

print(mycursor)

mycursor.execute("SELECT employees.*, departments.* FROM dept_manager INNER JOIN employees ON employees.emp_no = dept_manager.emp_no INNER JOIN departments ON departments.dept_no = dept_manager.dept_no")
row_headers=[x[0] for x in mycursor.description]
results = mycursor.fetchall()
json_data=[]
for result in results:
    json_data.append(dict(zip(row_headers,result)))

with open("dept.json", "w") as write_file:
    json.dump(json_data, write_file, indent=4, separators=(", ", ": "), sort_keys=True, default=str)

cnx.close()