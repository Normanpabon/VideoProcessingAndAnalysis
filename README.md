# Video processing and analysis

for now the program is in charge of dividing the video into frames, to then analyze one by one and define the object or objects that are in it,
it is mainly intended to identify people in the video and optimize time when reviewing security videos.


# Requeriments

- Python +3.6
- opencv-python (install using pip install opencv-python)
- yolo3.weights (you can get the file here: https://pjreddie.com/media/files/yolov3.weights)
- shutil
- matplotlib


# Usage

- Download the yolo3.weights file and place it in "VideoProcesingProject" folder
- Put the videos that you want to parse in "InputVideos" Folder
- Just run "VideoProcesing.py" and wait for the program to finish
- The output folder is "Prediction"
