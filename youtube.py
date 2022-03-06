# download a youtube video using pytube library

# pytube documentation - https://pytube.io/en/latest/
# ---------------------------------------------------
# Working with a single video

# import YouTube module/class
from pytube import YouTube

# copy paste video url you wish to download
url = 'https://www.youtube.com/watch?v=WjoplqS1u18'

# a basic command to download a video
YouTube(url).streams.first().download()
# however, this will download a low resolution version of the video

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

# get highest resolution
# add .download() to download the spicified stream
video_streams.get_highest_resolution()
# ---------------------------------------------------
# working with a playlist
from pytube import Playlist
p = Playlist('https://www.youtube.com/playlist?list=PLTLIGOWbZcEcP2yD-epNghnXsZlLAz9ml')

path = 'youtube_download/'
for url in p.video_urls:
    try:
        video = YouTube(url)
    except:
        print("Connection Error")
    video.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().download(path)
# ---------------------------------------------------
# working with a channel
from pytube import Channel
c = Channel('https://www.youtube.com/channel/UCMUnInmOkrWN4gof9KlhNmQ')

for video in c.videos:
	video.streams.get_highest_resolution().download()

# get urls from a channel
for url in c.video_urls[:3]:
	print(url)


# ---------------------------------------------------
# Using the search feature
from pytube import Search

s = Search('python')
# how many videos are there in this search?
len(s.results)
# list all videos objects with video ID
s.results
