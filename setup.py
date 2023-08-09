import setuptools

with open("README.md", "r", encoding="utf-8") as fhand:
    long_description = fhand.read()

setuptools.setup(
    name="playlistdl",
    version="0.0.1",
    author="Marvellous Chimaraoke",
    author_email="rokemarvellous@gmail.com",
    description=("An over-simplified package for "
                "downloading youtube playlists"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/0xMarvell/playlist-dl",
    project_urls={
        "Bug Tracker": "https://github.com/0xMarvell/playlist-dl/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pytube"],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "playlistdl = downloader.cli:main",
        ]
    }
)