import os, cv2
import numpy as np
import shutil as sht
from VideoFramesExtractor import ExtractVideoFrames
import matplotlib.pyplot as plt



def ParseImage(imgFile, rootDirectory, imgDirectory, UserSelection):
    UserSelectionFound = 0
    # load YOLO
    absolutePath = rootDirectory
    net = cv2.dnn.readNet(absolutePath+'/yolov3.weights', absolutePath+'/yolov3.cfg')
    classes = []

    with open(absolutePath+'/coco.names', "r") as f:
        classes = [line.strip() for line in f.readlines()]

    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    # Loading image
    print("DEBUG ", str(imgFile))
    img = cv2.imread(imgFile)
    img = cv2.resize(img, None, fx=0.4, fy=0.4)
    height, width, channels = img.shape

    # Detecting objects
    # 416 x 416 img size, 609 x 609 ideal but more proccesing time required
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Showing informations on the screen
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.4:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    # remove multiple boxes
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            label = str(classes[class_ids[i]]) #label is the detection name
            if(label == UserSelection):
                color = colors[i]
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 1)
                #cv2.putText(img, label, (x, y + 30), font, 3, color, 3)
                UserSelection = 1


    #cv2.imshow("Image", img)    # Indicates path and change method to cv2.imwrite(name, img)

    #os.chdir('Prediction')

    if UserSelection == 1:
        print('\n'+str(imgDirectory))
        actualDir = os.getcwd()
        filename = "Prediction"+imgDirectory+str(imgFile)
        cv2.imwrite(filename, img) #saves img
        os.chdir(absolutePath+'/Prediction')

        if os.path.isdir(imgDirectory):
            pass
        else:
            os.mkdir(imgDirectory)
        os.chdir(actualDir)
        sht.move(filename ,absolutePath+"/Prediction/"+imgDirectory+'/'+filename) #move the file to prediction folder
        cv2.destroyAllWindows()

    else:
        cv2.destroyAllWindows()



