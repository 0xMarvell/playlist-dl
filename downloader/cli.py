
"""
The command-line interface for the downloader
"""
import argparse
from .downloader import download_playlist


def main():
    parser = argparse.ArgumentParser(
        description=(
        "An over-simplified package for downloading youtube playlists.\n"
        "Downloaded videos are stored in the default downloads folder of the device."
        )
    )
    parser.add_argument(
        "url", type=str,
        help="The URL of the youtube playlist to be downloaded."
    )
    parser.add_argument(
        "--resolution", "-r", type=str,
        help=("Preferred video resolution for the youtube playlist.\n"
              "Available options are 720p, 480p, 360p, 240p, 144p.")
    )
    args = parser.parse_args()
    download_playlist(args.url, args.resolution)

if __name__ == "__main__":
    main()