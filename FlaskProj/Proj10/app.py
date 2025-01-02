from flask import Flask,render_template, request



app = Flask(__name__)


@app.route('/')

def home():
    return """<h1>Uplaod Images here</h1> <a href='/upload'>Upload Page</a>"""

@app.route('/upload')
def upload():
    return """<form method='POST'>
        <input type='file' />

</form>"""