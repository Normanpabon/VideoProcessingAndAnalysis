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
title = """
 _     _  ____  _________    ____  ____  ____  ____  _________  ____  _  _     _____   _____  ____  ____  _
/ \ |\/ \/  _ \/  __/  _ \  /  __\/  __\/  _ \/   _\/  __/ ___\/ ___\/ \/ \  //  __/  /__ __\/  _ \/  _ \/ \
| | //| || | \||  \ | / \|  |  \/||  \/|| / \||  /  |  \ |    \|    \| || |\ || |  _    / \  | / \|| / \|| |
| \// | || |_/||  /_| \_/|  |  __/|    /| \_/||  \_ |  /_\___ |\___ || || | \|| |_//    | |  | \_/|| \_/|| |_/\
\__/  \_/\____/\____\____/  \_/   \_/\_\\____/\____/\____\____/\____/\_/\_/  \\____\    \_/  \____/\____/\____/

"""

def createFolders():
    Iv = 0
    Pd = 0
    DirList = os.listdir()
    for dirs in DirList:
        if dirs == "InputVideos":
            Iv = 1
        if dirs == "Prediction":
            Pd = 1
    if Iv == 0:
        os.mkdir("InputVideos")
    if Pd == 0:
        os.mkdir("Prediction")





def ListImgFiles(wikiti):
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
    print(title)
    print("\n Select a object to find in videos and then press enter")
    Selected = int(input("\nSelect a option (1-6) \n 1.Pearsons \n 2.Dogs \n 3.cat \n 4.Cars \n 5.Motorbikes \n 6.Traffic Light\n==: "))

    if Selected == 1:
        wikiti = "person"
    if Selected == 2:
        wikiti = "dog"
    if Selected == 3:
        wikiti = "cat"
    if Selected == 4:
        wikiti = "car"
    if Selected == 5:
        wikiti = "motorbike"
    if Selected == 6:
        wikiti = "traffic light"

    input("\n Put the video files in 'InputVideos' folder and then press enter")




    ListVideoFiles()

    ExtractFrames()

    ListImgFiles(wikiti)



run()
