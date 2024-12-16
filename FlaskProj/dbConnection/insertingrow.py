import MySQLdb

conn = MySQLdb.connect(host='localhost', database='sindhunibas', user='root', password='Jeeban@12345')

cursor = conn.cursor()

def insertStudentData(id, name, address, phone):
    insert = "insert into students(id, name, address, phone) values(%s, %s, %s, %s)"
    try:
        cursor.execute(insert,(id,name,address,phone))
        conn.commit()
        print("one row inserted.")
    except MySQLdb.Error as e:
        print("Failed to insert: ", e)
        conn.rollback()


while True:
    choice = input("Enter insert or none: ")
    if(choice != 'insert'):
        break
    id = int(input("Enter id: "))
    name = input("Enter name: ")
    address = input("Enter address: ")
    phone = int(input("Enter Phone number: "))
    insertStudentData(id, name, address, phone)
    
    
# cursor.execute("Select * from students")
# rows = cursor.fetchall()

# for row in rows:
#     print(f"{row[0]:<10} {row[1]:<15} {row[2]:<10}")
    
cursor.close()
conn.close()