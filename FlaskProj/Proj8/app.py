from flask import Flask,url_for, redirect, request
import MySQLdb
app = Flask(__name__)

conn = MySQLdb.connect(host='localhost',user='root', database='sindhunibas',password='Jeeban@12345')

cursor = conn.cursor()



@app.route('/')
def home():
    cursor.execute("select * from employees")
    html_temp = """ <table border="1">
        <tr>
            <th>Id</th>
            <th>Name</th>
            <th>Salary</th>
            <th>Department</th>
        </tr>
        """
    rows = cursor.fetchall()
    for row in rows:
        html_temp += f""" 
        <tr>
            <td>{row[0]}</td>
            <td>{row[1]}</td>
            <td>{row[2]}</td>
            <td>{row[3]}</td>
        </tr>
        """
    html_temp += "</table>"
    html_temp += f"""<form action='{url_for('add')}' method='POST'>
        <input type='text' placeholder='Enter id' required name='id'><br>
        <input type='text' placeholder='Enter name' required name='name'><br>
        <input type='text' placeholder='Enter salary' required name='salary'><br>
        <input type='text' placeholder='Enter department' required name='department'><br>
        <input type='submit' value='Submit'>
    </form>"""
    return html_temp

@app.route('/add',methods=["POST"])
def add():
    id = int(request.form['id'])
    name = request.form['name']
    salary = float(request.form['salary'])
    department = request.form['department']
    try:
        query = "insert into employees(id, name, salary, department) values(%s,%s,%s,%s)"
        cursor.execute(query,(id,name,salary,department))
        conn.commit()
    except MySQLdb.Error as e:
        conn.rollback()
        return f"{e}"
    return redirect('/')
    


if __name__ == "__main__":
    app.run(debug=True)