from pytubefix import YouTube
from pytubefix.cli import on_progress

def download_video(url):
        try:
            yt = YouTube(url, on_progress_callback=on_progress)
            
            print("Title:", yt.title)
            print("Views:", yt.views)
    
            # Get the highest resolution stream
            yd = yt.streams.get_highest_resolution()
            
            # Download the video to the current directory
            yd.download()
            
            print("Download complete.")
        except Exception as e:
            print("An error occurred:", str(e))

def download_audio(url):
        try:
            yt = YouTube(url, on_progress_callback=on_progress)

            # Get highest bitrate audio stream for given codec (defaults to mp4)
            yd = yt.streams.get_audio_only()
            
            # Download the audio in .mp4 extention to the current directory
            yd.download()
            
            print("Download complete.")
        except Exception as e:
            print("An error occurred:", str(e))

# Ask the user to input the YouTube URL
url = input("Enter the YouTube URL: ")
download_video(url)
  