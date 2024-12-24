from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import uuid as uuid

app = Flask(__name__)

IMAGE_UPLOAD = os.path.join(os.getcwd(),'static','image')
app.config['IMAGE_UPLOAD'] = IMAGE_UPLOAD

# if not os.path.exists(IMAGE_UPLOAD):
#     os.makedirs(IMAGE_UPLOAD)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        f = request.files['image']
        fileNam, ext = os.path.splitext(secure_filename(f.filename))
        uniqueFileName = f"{fileNam}_{uuid.uuid4().hex}{ext}"
        filePath = os.path.join(app.config['IMAGE_UPLOAD'],uniqueFileName)
        f.save(filePath)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True,)