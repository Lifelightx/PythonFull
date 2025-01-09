from flask import Flask, render_template, request, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'static/upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 4 * 1024 * 1024  # 4 MB max file size
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Store uploaded image URLs
upload_images = []

@app.route('/')
def home():
    return """<h1>Upload Images Here</h1> <a href='/upload'>Upload Page</a>"""

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    global upload_images  # Access the global list of uploaded images

    if request.method == 'POST':
        # Handle file upload
        if 'image' in request.files:
            file = request.files['image']
            if file.filename:  # Check if a file is selected
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                file_url = url_for('static', filename=f'upload/{filename}')
                upload_images.append(file_url)  # Add image URL to the list
                print(upload_images)  # Debugging: Print the list of uploaded images
    
    # Generate HTML for uploaded images
    imagesTo = "".join(
        f"<img src='{i}' alt='Uploaded Image' height='100' width='200'>" for i in upload_images
    )

    # Return the form with the uploaded images
    return f"""
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="image" accept="image/*">
        <button type="submit">Upload</button>
        <div>
            {imagesTo}
        </div>
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)
