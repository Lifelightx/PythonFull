import MySQLdb

try:
    conn = MySQLdb.connect(host='localhost', user='root', password='Jeeban@12345', database='sindhunibas')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20))')
    def insertToUser(id, name):
        try:
            str = "INSERT INTO users(id, name) values(%s, %s)"
            cursor.execute(str,(id,name))
            conn.commit()
            print("one row inserted successfully.")
        except MySQLdb.Error as e:
            conn.rollback()
            print("Insertion Failed..:",e)
    
    while True:
        choice = input("Enter insert or none: ")
        if choice != 'insert':
            break
        id = int(input("Enter Id: "))
        name = input("Enter name: ")
        insertToUser(id,name)
    
    cursor.execute("UPDATE users set name='Jack Sparo' where id='110'")
    conn.commit()
    

except MySQLdb.Error as e:
    print("An error occurd: ", e)
    
finally:
    cursor.close()
    conn.close()