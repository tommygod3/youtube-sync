import os, re
from mutagen.mp3 import EasyMP3

class Formatter():
    songname_pattern = re.compile(r"^(?P<title>.*)_(?P<track>.*)_(?P<artist>.*)_(?P<album>.*)_(?P<date>.*).mp3$")

    def __init__(self):
        for filename in os.listdir("."):
            if filename.endswith('.mp3'):
                match = self.songname_pattern.match(filename)
                if match:
                    if match.group("track") != "NA":
                        track = match.group("track")
                    else:
                        track = match.group("title")
                    audio = EasyMP3(filename)
                    for group in ["artist", "album", "date"]:
                        audio[group] = match.group(group) if match.group(group) != "NA" else ""
                    audio.save()

                    os.rename(filename, f"{track}.mp3")
