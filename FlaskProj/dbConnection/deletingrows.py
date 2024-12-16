import MySQLdb
try:
    conn = MySQLdb.connect(host='localhost', database='sindhunibas', user='root', password='Jeeban@12345')
    cursor = conn.cursor()
    cursor.execute("delete from students where id=111")
    conn.commit()

    cursor.execute("select * from students")
    rows = cursor.fetchall()

    for i in rows:
        print(i)
except MySQLdb.Error as e:
    print(e)
    
cursor.close()
conn.close()