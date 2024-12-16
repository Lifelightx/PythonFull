import MySQLdb


try:
    conn = MySQLdb.connect(host = 'localhost', user='root', database='sindhunibas',password='Jeeban@12345')

    cursor = conn.cursor()

    cursor.execute("select * from students where id = 111")

    rows = cursor.fetchall()
    
    for i in rows:
        sId = i[0]
        sName = i[1]
        sAddress = i[2]
        print(f"{sId:<10} {sName:<15} {sAddress:<14}")
        
        
    print("All number of rows: ",cursor.rowcount)
    for i in rows:
        print(i)
except MySQLdb.Error as e:
    print(e)
    
finally:
    cursor.close()
    conn.close()