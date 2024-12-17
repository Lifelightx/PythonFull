from flask import Flask, request, render_template, redirect, url_for, jsonify
import MySQLdb
import  bcrypt

conn = MySQLdb.connect(host='localhost', user='root', database='sindhunibas', password='Jeeban@12345')

cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS websites (email VARCHAR(20) PRIMARY KEY, password VARCHAR(255))')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        print("Exucuted")
        data = request.get_json()
        if not data:
            return jsonify({'success':False,'message':'No data provided'}), 400
        email = data.get('email')
        try:
             cursor.execute("select * from websites where email = %s",(email,))
             existUser = cursor.fetchone()
             if existUser:
                return jsonify({"success":False,"message":"User Exists"})  
        except Exception as e:
            print("Error", e)
        password = data.get('password')
        hashpassword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        try:
            cursor.execute("insert into websites(email, password) values(%s, %s)",(email,hashpassword.decode('utf-8')))
            conn.commit()
            return jsonify({'success':True})
        except Exception as e:
            conn.rollback()
            print("Exception: ", e)
        return jsonify({"success":False})
        
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    cursor.execute('Select * from websites where email = %s',(email,))
    user = cursor.fetchone()
    print(user)
    if not user:
        return jsonify({'success':False, 'message':"Invalid Credential"}) , 401
    if not bcrypt.checkpw(password.encode('utf-8'), user[1].encode('utf-8')):
        return jsonify({'success':False, 'message':"Email and Password are incorrect"}), 401
    return jsonify({'success':True, 'message':"User LogedIn"}) , 200
        
               
            
        
    
if __name__ == '__main__':
    app.run(debug=True)
