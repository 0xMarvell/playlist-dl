from pytube import Playlist
from pathlib import Path

def download_playlist(playlist_url, video_resolution):
    try:
        playlist = Playlist(playlist_url)
        playlist._video_regex = None  # This line is needed to avoid issues with the new regex

        print(f"Downloading playlist: {playlist.title}")
        
        output_path = str(Path.home()/"Downloads") + playlist.title
        # Create the output directory if it doesn't exist
        import os
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        download_count = 0
        for video in playlist.videos:
            try:
                video.streams.get_by_resolution(video_resolution).download(output_path)
                count += 1
                print(f"Downloaded: {download_count} {video.title}")
            except Exception as e:
                print(f"Error downloading {video.title}: {e}")

        print("Playlist download completed.")
    except Exception as e:
        print(f"Error: {e}")
