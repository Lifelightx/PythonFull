from flask import Flask, render_template, request, redirect, url_for
import MySQLdb
conn = MySQLdb.connect(user='root',host='localhost',password='Jeeban@12345',database='sindhunibas')
cursor = conn.cursor()
app = Flask(__name__)

@app.route('/')
def home():
    query = "select * from employees"
    cursor.execute(query)
    rows = cursor.fetchall()
    return render_template('index.html', rows=rows)

@app.route('/add', methods=['POST'])
def addEmpolyee():
    if request.method == 'POST':
        id = int(request.form['id'])
        name = request.form['name']
        salary = float(request.form['salary'])
        department = request.form['department']
        if id != None and name != None and salary != None and department !=None:
            query = "insert into employees(Id, name, salary, department) values(%s,%s,%s,%s)" 
            try:
                cursor.execute(query, (id,name,salary,department))
                conn.commit()
            except MySQLdb.Error as e:
                conn.rollback()
                print(e)
                return redirect('/')
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)