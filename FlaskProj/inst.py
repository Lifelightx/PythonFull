import instaloader
import os
import shutil

# Create an instance of Instaloader
loader = instaloader.Instaloader()

# Configure Instaloader to download only videos
loader.download_comments = False
loader.save_metadata = False
loader.post_metadata_txt_pattern = ""

# Function to download Instagram video
def download_instagram_video(url):
    try:
        # Extract the shortcode from the URL
        shortcode = url.split("/")[-2]

        # Get the Downloads folder path
        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

        # Temporary folder for downloading
        temp_folder = "temp_instagram_download"
        os.makedirs(temp_folder, exist_ok=True)

        # Change the target folder for download
        loader.dirname_pattern = temp_folder

        # Download the post
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        loader.download_post(post, target=".")

        # Move the video file to the Downloads folder
        for file in os.listdir(temp_folder):
            if file.endswith(".mp4"):
                dest_path = os.path.join(downloads_folder, file)
                shutil.move(os.path.join(temp_folder, file), dest_path)
                print(f"Video saved in Downloads folder: {dest_path}")

        # Clean up unnecessary files and folder
        shutil.rmtree(temp_folder)

    except Exception as e:
        print("An error occurred:", e)

# Example usage
if __name__ == "__main__":
    instagram_url = input("Enter the Instagram video URL: ")
    download_instagram_video(instagram_url)
