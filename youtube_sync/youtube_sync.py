from docopt import docopt

usage = """
youtube_sync.py

Usage:
    youtube-sync
    youtube-sync ffmpeg
    youtube-sync ffmpeg set PATH

Options:
  -h --help     Show this screen.
  --version     Show version.

"""
def main():
    args = docopt(usage)
    print(args)

if __name__ == "__main__":
    main()
