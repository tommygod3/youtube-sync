import json
from pathlib import Path

class ConfigHandler():
    def __init__(self, cli_args):
        self.global_config_path = Path(f"~/.config/youtube-sync/config.json").expanduser()
        self.repo_config_path = Path(f"./repo-config.json")

        self.global_config = self.get_config(self.global_config_path)
        self.repo_config = self.get_config(self.repo_config_path)

        if cli_args["ffmpeg"]:
            if cli_args["set"]:
                self.global_config["ffmpeg_path"] = cli_args["PATH"]
            else:
                print(self.global_config["ffmpeg_path"] if self.global_config.get("ffmpeg_path") else "ffmpeg location not set")

        if cli_args["url"]:
            if cli_args["set"]:
                self.repo_config["url"] = cli_args["URL"]
            else:
                print(self.repo_config["url"] if self.repo_config.get("url") else "url not set")
    
    def get_config(self, path: Path):
        if not path.exists():
            return {}
        with open(path) as reader:
            return json.load(reader)

    def __del__(self):
        self.global_config_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.global_config_path, "w") as writer:
            json.dump(self.global_config, writer)
        
        with open(self.repo_config_path, "w") as writer:
            json.dump(self.repo_config, writer)
