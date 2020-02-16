from docopt import docopt

from config_handler import ConfigHandler

usage = """
youtube_sync.py

Usage:
    youtube-sync
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
    ConfigHandler(args)

    print(args)

if __name__ == "__main__":
    main()
