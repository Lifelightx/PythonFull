import instaloader
import os
import shutil
from flask import Flask, render_template, redirect, request, url_for
import threading
import time

# Initialize Instaloader
loader = instaloader.Instaloader()

# Configure Instaloader to download only videos
loader.download_comments = False
loader.save_metadata = False
loader.post_metadata_txt_pattern = ""

# Get the base directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VIDEO_FOLDER = os.path.join(BASE_DIR, "static", "videos")

# Ensure the folder exists
os.makedirs(VIDEO_FOLDER, exist_ok=True)


def clean_folder_after_delay(delay=120):
    """Deletes all files from the video folder after the specified delay."""
    time.sleep(delay)
    for file in os.listdir(VIDEO_FOLDER):
        file_path = os.path.join(VIDEO_FOLDER, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
    print("Cleaned up video folder.")


def download_instagram_video(url):
    try:
        # Extract the shortcode from the URL
        shortcode = url.split("/")[-2]

        # Set Instaloader's download directory
        loader.dirname_pattern = "."

        # Download the post
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        loader.download_post(post, target="temp")

        # Rename and move the video file to the static/videos folder
        for file in os.listdir("temp"):
            if file.endswith(".mp4"):
                custom_name = f"InstagramVideo_{shortcode}.mp4"
                dest_path = os.path.join(VIDEO_FOLDER, custom_name)
                shutil.move(os.path.join("temp", file), dest_path)
                print(f"Video saved: {dest_path}")
                # Clean up the temporary folder
                shutil.rmtree("temp", ignore_errors=True)
                return os.path.join("static", "videos", custom_name)
    except Exception as e:
        print("Error: ", e)
    return None


# Flask App
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/download", methods=["POST"])
def download():
    if request.method == "POST":
        vdo_url = request.form["urlText"]
        video_url = download_instagram_video(vdo_url)
        if video_url:
            # Start a background thread to clean up files after 2 minutes
            threading.Thread(target=clean_folder_after_delay).start()
            return render_template("video.html", video_url=video_url)
        return "Error: Unable to download the video.", 500


if __name__ == "__main__":
    app.run(debug=True)
