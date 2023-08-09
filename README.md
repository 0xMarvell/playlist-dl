# PlaylistDL 📹

PlaylistDL is really just a basic python script for downloading youtube playlists all at once. It solves the problem of wasting an unnecessary amount of time on downloading videos one by one.
It makes use of the [pytube](https://pytube.io/en/latest/index.html) library.

## Install PlaylistDL

- If not already installed, download and install [Python](https://www.python.org/downloads/).
- Download zip file `playlistdl-0.0.1.zip` from repo
- Install through command line

    ```bash
    cd Downloads
    sudo pip3 install playlistdl-0.0.1.zip //mac OS or linux
    pip install playlistdl-0.0.1.zip //windows
    ```

## How to use PlaylistDL

- Help

    ```bash
    playlistdl -h
    ```

- Downloading a playlist:

    ```bash
    playlistdl <url> -r <resolution>
    ```

  - Example

    ```bash
    playlistdl https://www.youtube.com/playlist?list=PLOLrQ9Pn6caz-6WpcBYxV84g9gwptoN20 -r 720p
    ```

### Uninstalling PlaylistDL

```bash
sudo pip3 uninstall playlistdl //macOS or linux
pip uninstall playlistdl //windows
```
