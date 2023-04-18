import mysql.connector

connection = mysql.connector.connect(user='root', database='bank', password='antonio2008.')

cursor = connection.cursor()

testQuery = ("SELECT * FROM info")

cursor.execute(testQuery)

for item in cursor:

    print(item)

cursor.close()

connection.close()

 