import time
import queue
import subprocess
import threading
import os

inputQueue = queue.Queue()

completePool = []

inputDirectoryPath = "C:\\Galaxy\\Scripts\\500\\Ex2\\InputVideos"
for filename in os.listdir(inputDirectoryPath):
    inputQueue.put(filename)

def processVideo():
    while not inputQueue.empty():
        filename = inputQueue.get()
        filePath = "InputVideos\\" + filename
        outputFilePath = "OutputVideos\\" + filename[:-4] + "modified.mp4"
        threadName = threading.currentThread().getName()
        print("processing: " + filename + " on " + threadName + "\n")
        # subprocess.call("ffmpeg -i " + filePath + " -c:a copy -s hd480 -b:v 1M -r 30 " + outputFilePath, shell=True)
        time.sleep(10)
        print( filename + " complete\n")
        completePool.append(filename)

    print(threadName + " done\n")

threadOne = threading.Thread(name = "One", target = processVideo)
threadTwo = threading.Thread(name = "Two", target = processVideo)
threadThree = threading.Thread(name = "Three", target = processVideo)

threadOne.start()
threadTwo.start()
threadThree.start()
