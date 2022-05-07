pytube Command-line interface (CLI)

To download the highest resolution progressive stream:

$ pytube url

To view available streams:

$ pytube url --list

To download a specific stream, use the itag

$ pytube url --itag=22

To get a list of all subtitles (caption codes)

$ pytube url --list-captions

To download a specific subtitle (caption code) - in this case the English subtitles (in srt format) - use:

$ pytube url -c en

It is also possible to just download the audio stream (default AAC/mp4):

$ pytube url -a

To list all command line options, simply type

$ pytube --help
