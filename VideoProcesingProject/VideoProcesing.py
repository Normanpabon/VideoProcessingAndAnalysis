import os
from VideoFramesExtractor import ExtractVideoFrames
from OpenCvManager import ParseImage
import matplotlib.pyplot as plt

options = {
    'model': 'cfg/t'
}
rootDirectory = os.getcwd()
videoFiles = []
photoDirectories = []
photoFiles = []
wikiti = "person" #change for user selection

def ListImgFiles():
    os.chdir("InputVideos")
    InputDirectory = os.getcwd()
    DirList = os.listdir()
    for dir in DirList:     #obtiene los directorios generados
        if os.path.isdir(dir):
            photoDirectories.append(dir)
    i = 0
    for loc in photoDirectories: # separa directorios de archivos de videos
        os.chdir(loc)

        for x in os.listdir():

            photoFiles.append(x)

        for photos in photoFiles: # coge cada archivo de imagen del directorio

            ParseImage(photos, rootDirectory, loc, wikiti)

        photoFiles.clear()
        print("Vuelta " + str(i))
        os.chdir(InputDirectory)
        i +=1



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





def run():
    ListVideoFiles()
    ExtractFrames()
    ListImgFiles()



run()
