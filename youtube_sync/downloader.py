import yt_dlp

class Downloader():
    def __init__(self, config):
        self.config = config

        ydl_options = {
            "download_archive": "archive.txt",
            "ffmpeg_location": self.config.global_config["ffmpeg_path"],
            "playlistreverse": True,
            "outtmpl": "%(title)s_%(track)s_%(artist)s_%(album)s_%(release_year)s.%(ext)s",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }]
        }

        with yt_dlp.YoutubeDL(ydl_options) as ydl:
            ydl.download([self.config.repo_config["url"]])
