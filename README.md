# chapters2videos
Simple yet useful script setup to add custom chapters to your personal videos or downloaded ones... 

## Usage Steps:
- Extract Metadata from your file by: ```ffmpeg -i INPUT.mp4 -f ffmetadata FFMETADATAFILE.txt```
- Run the following script by: ```python addChapters.py```
- Finishing by adding the chapters: ```ffmpeg -i INPUT.mp4 -i FFMETADATAFILE -map_metadata 1 -codec copy OUTPUT.mp4```
### Considerations:
- Your video needs to be named ```INPUT.mp4``` or just change the commands accordingly
- You'll need Python and ffmpeg library installed on your system and configured in PATH
- The script expects to be in the same directory as a 'chapters.txt' file to read from, and an 'FFMETADATAFILE' file to output to.
- It expects the chapters.txt file to be a txt file with 1 chapter per line starting with 00:00:00 style time stamps and followed by the title of the chapter
- It appends to an existing FFMETADATAFILE
- It expects no existing chapters in the file
- It expects an final END chapter which is ignored, but provides the end point for the last real chapter.


