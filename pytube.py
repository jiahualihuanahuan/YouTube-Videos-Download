# download a youtube video using pytube library

# pytube documentation - https://pytube.io/en/latest/
# github site: https://github.com/pytube

Please visit this issue to solve "pytube.exceptions.RegexMatchError: get_throttling_function_name: could not find match for multiple" issue
https://github.com/pytube/pytube/issues/1289

This new file comment out line 272 and line 273

line 275: 
	
File cur: r'\([a-z]\s*=\s*([a-zA-Z0-9$]{3})(\[\d+\])?\([a-z]\)',
	
File new: r'\([a-z]\s*=\s*([a-zA-Z0-9$]{2,3})(\[\d+\])?\([a-z]\)'

line 290: 
	
File cur: nfunc=function_match.group(1)),

File new: nfunc=re.escape(function_match.group(1))),
# ---------------------------------------------------
# Download a single video

# import YouTube module/class
from pytube import YouTube

# copy paste video url you wish to download
url = 'https://www.youtube.com/watch?v=WjoplqS1u18'

# a basic command to download a video
YouTube(url).streams.first().download()
# however, this will download a low resolution version of the video

# get highest resolution

# add .download() to download the spicified stream
YouTube(url).streams.get_highest_resolution().download()

# create a YouTube object
video = YouTube(url)

# get video title
video.title

# get video author
video.author

# get video publish date
video.publish_date

# get video_id
video.video_id

# get thumbnail url
video.thumbnail_url

# get subtitle/caption tracks
video.captions # you can see how many caption languages are available

# get captions in a specific language
caption = video.captions['en-US']
caption.xml_captions

# convert to srt format
print(caption.generate_srt_captions()) # not working

# .streams will gives you all the stream types this video have, 
# for example, media format (mp4 etc.), resolution (1080p), 
# fps (frames per second, 60fps)
video_streams = YouTube(url).streams # this StreamQuery object cannot follow by .download()
# print(video_streams)

# we can filter the streams based on file_extension, resolution, fps etc.
video_streams.filter(file_extension='mp4')
video_streams.filter(progressive=True) # you can filter to only progressive streams
video_streams.filter(adaptive=True) #  if you only want to see the DASH streams (also referred to as “adaptive”)
video_streams.filter(only_audio=True)
video_streams.filter(res='4320p')

# specify which stream you would like to access/download
# add .download() to download the spicified stream
video_streams.first()
video_streams.last()
video_streams[0] # first
video_streams[-1] # last

# we can download a specific stream by itag ID
# add .download() to download the spicified stream
video_streams.get_by_itag(571)

# ---------------------------------------------------
# download only 1080p and audio files, 
# YouTube(url).streams.get_highest_resolution().download() will only get 720p video
from pytube import YouTube
from pytube import Playlist

pid = "PLSIJismKOisFCjrj2lspg4_J65-BEK4Di"
url = f"https://www.youtube.com/playlist?list={pid}"

path = "./向风而行/"

p = Playlist(url)

for url in p.video_urls:
    try:
        video = YouTube(url)
    except:
        print("Connection Error")
        
    try:
        print(f"downloading {video.streams[0].title}")
        video.streams.filter(res='1080p', file_extension='mp4').get_by_itag(137).download(path)
        video.streams.get_by_itag(251).download(path)
        print(f"downloaded {video.streams[0].title}")
    except:
        print("Video Error")

# ---------------------------------------------------
# working with a playlist
from pytube import Playlist

id = "PLsXPnEADaW-Ta1GW8QfwaBZfk5GNvkoiZ"

url = f"https://www.youtube.com/playlist?list={id}"
p = Playlist(url)

path = 'your/path/to/store/videos'
for url in p.video_urls:
    try:
        video = YouTube(url)
    except:
        print("Connection Error")
    print(f"downloading {video.streams[0].title}")
    video.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().download(path)
    print(f"downloaded {video.streams[0].title}")
# ---------------------------------------------------
# working with a channel
from pytube import Channel
from datetime import datetime

url = "https://www.youtube.com/c/lexfridman"
c = Channel(url)

print("Start Downloading Youtube Videos from Lex Fridman")

path = "K:/Youtube_Video/Lex Fridman"

for video in c.videos:
    try: 
        start_time = datetime.now()
        print(f"start time {start_time}")
        print(f"downloading {video.streams[0].title}")
        video.streams.get_highest_resolution().download(path)
        end_time = datetime.now()
        print(f"end time {end_time}")
        print(f"{video.streams[0].title} downloaded")
    except:
        print("Connection Error")


# ---------------------------------------------------
# Using the search feature
from pytube import Search

search_words = "python analytics"

s = Search(search_words)
# how many videos are there in this search?
len(s.results)
# list all videos objects with video ID
s.results
# get more search results if there are any
s.get_next_results()
path = '/'
for video in s.results:
    video.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().download(path)

#------------------------------------------------------
# download audio only using filter(only_audio=True) 
from pytube import YouTube
from pytube import Playlist
import subprocess
import os

pid = "OLAK5uy_noL7pbl2KRa4Jn854tTmHnNgAJumzzhU8"
url = f"https://www.youtube.com/playlist?list={pid}"

path = "D:/Media/Music/陶心瑤"

p = Playlist(url)

for url in p.video_urls:
    try:
        video = YouTube(url)
    except:
        print("Connection Error")
        
    try:
        print(f"downloading {video.streams[0].title}")
        print(video.streams.filter(only_audio=True)[-1])
        video.streams.filter(only_audio=True)[-1].download(path)
        print(f"downloaded {video.streams[0].title}")
    except:
        print("Video Error")

	
#------------------------------------------------------
# Using the search feature to download audio only
from pytube import Search

search_words = "于文文"

s = Search(search_words)
# how many videos are there in this search?
len(s.results)
# list all videos objects with video ID
s.results
# get more search results if there are any
s.get_next_results()
s.get_next_results()
s.get_next_results()
s.get_next_results()
path = "D:/Media/Music/于文文"
try:
    for video in s.results:
        try:
            print(f"downloading {video.streams[0].title}")
            print(video.streams.filter(only_audio=True)[-1])
            video.streams.filter(only_audio=True)[-1].download(path)
            print(f"downloaded {video.streams[0].title}")
        except:
            print("Video Error")
except:
    print("Connection Error")
