import os, re
from mutagen.mp3 import EasyMP3



regex_old = re.compile(r"^(?P<title>.*) - (?P<name>.*)-(?P<mess>.{11}).mp3$")
regex_new = re.compile(r"^(?P<name>.*) - (?P<title>.*)-(?P<mess>.{11}).mp3$")

for filename in os.listdir("."):
    if '.mp3' in filename:
        print(f"Old name: {filename}")
        match_old = regex_old.match(filename)
        match_new = regex_new.match(filename)
        if filename.startswith("H3") and match_old:
            print(f"Mess: {match_old.group('mess')}")
            new_name = f"{match_old.group('title')} - {match_old.group('name')}.mp3"
            os.rename(filename, new_name)
            filename = new_name
            print(f"New name: {new_name}")
        elif match_new:
            print(f"Mess: {match_new.group('mess')}")
            new_name = f"{match_new.group('title')} - {match_new.group('name')}.mp3"
            os.rename(filename, new_name)
            filename = new_name
            print(f"New name: {new_name}")
        else:
            print(f"No change: {filename}")

        audio = EasyMP3(filename)
        audio["artist"] = "H3"
        audio["album"] = "H3 Podcast"
        audio.save()
