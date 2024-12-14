import MySQLdb


try:
    conn = MySQLdb.connect(host = 'localhost', user='root', database='sindhunibas',password='Jeeban@12345')

    cursor = conn.cursor()

    cursor.execute("select * from students")

    rows = cursor.fetchall()

    for i in rows:
        print(i)
except MySQLdb.Error as e:
    print(e)
    
finally:
    cursor.close()
    conn.close()