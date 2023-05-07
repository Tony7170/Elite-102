import mysql.connector

conn = mysql.connector.connect(user='root', database='bank', password='antonio2008.')

cursor = conn.cursor()

acc_bal = 100

testQuery = ("UPDATE info SET Balance = (%s)")

cursor.execute(testQuery, (acc_bal,))

conn.commit()

balance = cursor.fetchall()

print(balance)

cursor.close()

conn.close()
