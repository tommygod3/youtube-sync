# youtube-sync
Simple wrapper around youtube-dl to cleanly download a playlist of songs

## Installation
```bash
pip install git+https://github.com/tommygod3/youtube-sync.git
```

## Usage
Make sure you have set the path to ffmpeg:
```bash
youtube-sync ffmpeg set PATH
```
This will saved for future use in your home directory at `~/.config/youtube-sync/config.json`

Navigate to a directory that you want to download a playlist into:
```bash
cd ~/Music/MyPlaylist
```

Set the url of the playlist that will be downloaded into the directory:
```bash
youtube-sync url set URL
```
This will saved in a `repo-config.json` in the directory

Download the playlist:
```bash
youtube-sync download
```
