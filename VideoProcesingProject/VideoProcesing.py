import os, wget
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
TotalFiles = 0
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


def checkRequirements():
    yoloExists = 0
    FilesInRoot = os.listdir()
    for file in FilesInRoot:
        if file == "yolov3.weights":
            yoloExists = 1


    if yoloExists == 0:
        print("\n'Yolov3.weights' file not found, the file needs to be in project main directory \nDownload the missed file ? it can take arround 20 mins")
        downloadFile = str(input("\n Select a option (1-2)\n 1. Yes \n 2. Exit \n == "))
        if downloadFile == '1':
            print("\nStarting download... ")
            fileD = 'https://pjreddie.com/media/files/yolov3.weights'
            filename = wget.download(fileD)
            print("\nDownload completed succesfully")


        else:
            exit()



def PrintProgressBar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):

    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


def ListImgFiles(wikiti, TotalFiles):
    os.chdir("InputVideos")
    InputDirectory = os.getcwd()
    DirList = os.listdir()

    print('DEBUG TOTAL SIZE: '+str(TotalFiles))
    for dir in DirList:     #obtains the new directories
        if os.path.isdir(dir):
            photoDirectories.append(dir)
    i = 0
    z = 0
    for loc in photoDirectories: # splits video directories
        os.chdir(loc)
        for x in os.listdir():
            photoFiles.append(x)

        for photos in photoFiles: # takes every photo from the directory
            PrintProgressBar(iteration=z, total=TotalFiles, prefix = 'Progress:', suffix = 'Complete', length = 50)
            ParseImage(photos, rootDirectory, loc, wikiti)
            z += 1

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

def ListAllFiles():
    returnToFolder = os.getcwd()

    print('DEBUG FOLDER'+str(os.getcwd()))

    os.chdir(rootDirectory+'/InputVideos')
    directoryList = os.listdir()
    allFilesList = []
    for directory in directoryList:
        if os.path.isdir(directory):
            os.chdir(directory)
            filesinFolder = os.listdir()
            for files in filesinFolder:
                allFilesList.append(files)
            os.chdir(rootDirectory+'/InputVideos')
    os.chdir(returnToFolder)

    return len(allFilesList)





def run():
    print(title)

    createFolders()

    input("\n Put the video files in 'InputVideos' folder and then press enter")

    checkRequirements()

    ListAllFiles()

    TotalFiles = int(ListAllFiles())

    print("\n Select a object to find in videos and then press enter")
    Selected = int(input("\nSelect a option (1-6) \n 1.People \n 2.Dogs \n 3.cat \n 4.Cars \n 5.Motorbikes \n 6.Traffic Light\n==: "))

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






    ListVideoFiles()

    ExtractFrames()

    ListImgFiles(wikiti, TotalFiles)



run()
