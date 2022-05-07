# Download-YouTube-Videos
Provide python scripts that can download YouTube videos for educational/personal use

Library: pytube

Module: YouTube, Playlist, Channel, Search

Command-line interface (CLI)
Pytube also ships with a tiny CLI for interacting with videos and playlists.

To download the highest resolution progressive stream:

$ pytube https://www.youtube.com/watch?v=2lAe1cqCOXo
To view available streams:

$ pytube https://www.youtube.com/watch?v=2lAe1cqCOXo --list
To download a specific stream, use the itag

$ pytube https://www.youtube.com/watch?v=2lAe1cqCOXo --itag=22
To get a list of all subtitles (caption codes)

$ pytube https://www.youtube.com/watch?v=2lAe1cqCOXo --list-captions
To download a specific subtitle (caption code) - in this case the English subtitles (in srt format) - use:

$ pytube https://www.youtube.com/watch?v=2lAe1cqCOXo -c en
It is also possible to just download the audio stream (default AAC/mp4):

$ pytube https://www.youtube.com/watch?v=2lAe1cqCOXo -a
To list all command line options, simply type

$ pytube --help



# Download-YouTube-Transcripts
Provide python scripts that can download YouTube videos' transacirpts for educational/personal use

Library: youtube_transcript_api

Module: YouTubeTranscriptApi
