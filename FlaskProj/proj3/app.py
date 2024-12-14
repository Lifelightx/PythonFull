from flask import Flask, render_template, request, jsonify
import bcrypt as bc
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        name = request.form['name']
        mail = request.form['mail']
        password = request.form['password']
        secPass = bc.hashpw(password.encode('utf-8'), bc.gensalt(10))
        print(name,mail,secPass)
        return jsonify({"name":name, "mail":mail, "password":secPass.decode('utf-8')})
    return render_template('reg.html')

if __name__ == '__main__':
    app.run(debug=True)