import mysql.connector

connection = mysql.connector.connect(user='root', database='bank', password='antonio2008.')

cursor = connection.cursor()

testQuery = ('SELECT Balance FROM info')

cursor.execute(testQuery)

for item in cursor:
    for x in item:
        if x.isdigit:
            balance = x

print(balance)

cursor.close()

connection.close()
