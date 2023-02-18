from docopt import docopt

from .config_handler import ConfigHandler
from .downloader import Downloader

usage = """
youtube_sync.py

Usage:
    youtube-sync download
    youtube-sync ffmpeg
    youtube-sync ffmpeg set PATH
    youtube-sync url
    youtube-sync url set URL

Options:
  -h --help     Show this screen.
  --version     Show version.

"""
def main():
    args = docopt(usage)
    config = ConfigHandler(args)
    if args["download"]:
        Downloader(config)

if __name__ == "__main__":
    main()
