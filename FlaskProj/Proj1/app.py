from flask import Flask, render_template, jsonify

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')

def hello_world():
    return "<h1>Hello world</h1>"

@app.route('/home')

def home_page():
    return render_template('index.html')

@app.route('/data')
def data_page():
    return jsonify({"id":101,"name":"Jeeban", "message":"welcome to new flask page",'roll':'120021', 'pakc':'20002'})



if __name__ == '__main__':
    app.run(debug=True, port=5000)
