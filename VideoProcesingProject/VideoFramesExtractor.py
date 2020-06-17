# import numpy as np
import cv2, os


def ExtractVideoFrames(VideoName):
    directory = os.getcwd()
    os.chdir(directory + '/InputVideos')
    videoLocation = VideoName
    capture = cv2.VideoCapture(videoLocation)
    i = 0
    newFolderName = VideoName + 'Frames'
    if os.path.isdir(newFolderName):
        pass
    else:
        os.mkdir(newFolderName)
    directory = os.getcwd()
    os.chdir(directory + '/' + newFolderName)

    while (capture.isOpened()):
        ret, frame = capture.read()
        if ret == False:
            break
        cv2.imwrite('Frame' + str(i) + '.jpg', frame)
        i = i + 1
    capture.release()
    cv2.destroyAllWindows()
