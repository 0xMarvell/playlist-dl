from pytube import Playlist

def download_playlist():
    try:
        playlist = Playlist(input("Input the youtube playlist url: "))
        playlist._video_regex = None  # This line is needed to avoid issues with the new regex

        print(f"Downloading playlist: {playlist.title}")
        video_resolution = input("Select video resolution (720p, 480p, 360p, 240p, 144p): ")
        
        output_path = playlist.title
        # Create the output directory if it doesn't exist
        import os
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        for video in playlist.videos:
            try:
                video.streams.get_by_resolution(video_resolution).download(output_path)
                print(f"Downloaded: {video.title}")
            except Exception as e:
                print(f"Error downloading {video.title}: {e}")

        print("Playlist download completed.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    download_playlist()
