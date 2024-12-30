from flask import Flask,redirect,render_template,url_for,request,session
from werkzeug.security import generate_password_hash,check_password_hash
import MySQLdb 


def db_connect():
    conn = MySQLdb.connect(host='localhost', user='root', password='Jeeban@12345', database='newyeardb')
    return conn
    

app = Flask(__name__)


@app.route('/')

def home():
    return render_template('index.html')
@app.route('/signup', methods=['POST', 'GET'])
def getstarted():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        if not email or not password:
            # flash('Please enter your email or password')
            return redirect('/login')
        hashed_password = generate_password_hash(password)
        conn = db_connect()
        cursor = conn.cursor()
        querry = "insert into users(name, email, password)values(%s, %s,%s)" 
        try:
            cursor.execute(querry,(name,email,hashed_password))
            conn.commit()
            # flash("Registered successfully!")
            return redirect('/login')
        except MySQLdb.Error as e:
            # flash(f"Error: {e}")
            conn.rollback()
            
            return redirect(url_for('signup'))
        
        
        
    return render_template('signup.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if not email or not password:
            return redirect('/login')
        conn = db_connect()
        cursor = conn.cursor()
        try:
            querry = "select * from users where email=%s"
            cursor.execute(querry,(email))
            user = cursor.fetchone()
            if user and check_password_hash(user[3], password):
                # flash('Logged in successfully!')
                session['username'] = user[1]
                return redirect('/dashboard')
            else:
                # flash('Invalid email or password')
                return redirect('/login')
        except MySQLdb.Error as e:
            # flash(f"Error: {e}")
            return redirect(url_for('login'))
        finally:
            cursor.close()
            conn.close()   
    return render_template('login.html')

app.route('/dashboard')
def dashboard():
    

if __name__ == "__main__":
    app.run(debug=True)