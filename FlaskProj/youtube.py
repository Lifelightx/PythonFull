import yt_dlp

def download_video_yt_dlp(video_url, save_path=None):
    """
    Downloads a YouTube video using yt-dlp.
    """
    try:
        ydl_opts = {
            'outtmpl': save_path or '%(title)s.%(ext)s',  # Save with the video title
            'format': 'bestvideo+bestaudio/best',        # Get the best quality
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Download complete!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
video_url = "https://www.youtube.com/embed/Qmx4wqm0GZs?si=kvpdOPzfCQJ9MX7w"
download_video_yt_dlp(video_url)
