# Original source by Kyle Howells at https://ikyle.me/blog/2020/add-mp4-chapters-ffmpeg
# Modified/fixed by Danilo Nascimento at blablabla
# 
# Usage Steps:
# Extract Metadata from your file by: ffmpeg -i INPUT.mp4 -f ffmetadata FFMETADATAFILE.txt
# The script expects to be in the same directory as a 'chapters.txt' file to read from, and an 'FFMETADATAFILE' file to output to.
#     It expects the chapters.txt file to be a txt file with 1 chapter per line starting with 00:00:00 style time stamps and followed by the title of the chapter
#     It appends to an existing FFMETADATAFILE
#     It expects no existing chapters in the file
#     It expects an final END chapter which is ignored, but provides the end point for the last real chapter.
# run the following script by: python addChapters.py
# finishing by adding the chaprters: ffmpeg -i INPUT.mp4 -i FFMETADATAFILE -map_metadata 1 -codec copy OUTPUT.mp4


import re

chapters = list()

with open('chapters.txt', 'r') as f:
   for line in f:
      #re.match(r"(\d):(\d{2}):(\d{2}) (.*)", line)
      x = re.match(r"(\d{2}):(\d{2}):(\d{2}) (.*)", line)
      hrs =  int(x.group(1))
      mins = int(x.group(2))
      secs = int(x.group(3))
      title = x.group(4)

      minutes = (hrs * 60) + mins
      seconds = secs + (minutes * 60)
      timestamp = (seconds * 1000)
      chap = {
         "title": title,
         "startTime": timestamp
      }
      chapters.append(chap)

text = ""

for i in range(len(chapters)-1):
   chap = chapters[i]
   title = chap['title']
   start = chap['startTime']
   end = chapters[i+1]['startTime']-1
   text += f"""
[CHAPTER]
TIMEBASE=1/1000
START={start}
END={end}
title={title}
"""


with open("FFMETADATAFILE", "a") as myfile:
    myfile.write(text)
    print("COMPLETE!")