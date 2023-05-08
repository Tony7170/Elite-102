import mysql.connector

conn = mysql.connector.connect(user='root', database='bank', password='antonio2008.')

cursor = conn.cursor()

testQuery = ("SELECT Balance From info")
cursor.execute(testQuery)

result = cursor.fetchone()[0]

print (result)

conn.commit()

cursor.close()

conn.close()