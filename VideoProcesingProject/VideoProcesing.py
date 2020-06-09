import os
from VideoProcesingProject.VideoFramesExtractor import ExtractVideoFrames

rootDirectory = os.getcwd()
videoFiles = []


def ListVideoFiles():
    print("Listing video files\n")
    os.chdir('InputVideos')
    FileList = os.listdir()
    for file in FileList:
        if os.path.isfile(file):
            videoFiles.append(file)
    os.chdir(rootDirectory)


def ExtractFrames():
    videoList = videoFiles
    for video in videoList:
        print("Extracting frames from video : " + str(video) + "\n")
        ExtractVideoFrames(video)
        os.chdir(rootDirectory)
    print("Frames extracted correctly")

def CallDarknet():
    pass

def run():
    ListVideoFiles()
    ExtractFrames()


run()
