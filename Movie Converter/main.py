from moviepy.editor import *


print("Welcome to my Video Converter Tool")

# Retrieve the video clip into the variable
clip = VideoFileClip("videoclip.mp4")

#convert the clip file to gif
clip.write_gif("videoclip.gif")

print("Conversion completed")