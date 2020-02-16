import youtube_dl

class Downloader():
    def __init__(self, config):
        self.config = config

        ydl_options = {
            "format": "bestaudio/best",
            "ffmpeg_location": self.config.global_config["ffmpeg_path"],
            "playlistreverse": True,
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }]#TODO: Look into progress hooks
        }

        with youtube_dl.YoutubeDL(ydl_options) as ydl:
            ydl.download([self.config.repo_config["url"]])
