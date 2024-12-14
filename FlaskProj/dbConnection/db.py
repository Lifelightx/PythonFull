import MySQLdb

conn = MySQLdb.connect(host='localhost', database='sindhunibas', user='root', password='Jeeban@12345')

cursor = conn.cursor()
cursor.execute("select * from students")

row = cursor.fetchone()

# rows = cursor.fetchall()

while row is not None:
    print(row)
    row = cursor.fetchone() #get the next row

# for row in rows:
#     print(row)
cursor.close()
conn.close()

