import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='employees')
cursor = cnx.cursor()
query = "SELECT * FROM employees;"
cursor.execute(query)
data = cursor.fetchall()

data.sort(key=lambda x: (x[2], -x[1]))
data = data[::-1]
for row in data:
    print(row[0], row[2], row[1])