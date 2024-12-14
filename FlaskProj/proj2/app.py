from flask import Flask, render_template,jsonify

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/data')
def data_fetch():
    return jsonify({'name':"Jeebanjyoti Mallik", 'phone':'6371317325', 'empId':4125424})

if __name__ == '__main__':
    app.run(debug=True)