import subprocess

subprocess.call("ffmpeg -i InputVideos\\Gopro.mp4 -c:a copy -s hd480 -b:v 1M -r 30 OutputVideos\\output3.mp4", shell=True)
print("complete")
