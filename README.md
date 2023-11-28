# Sign Language Detection using YOLOv5

## Introduction
The Sign Language Detection project focuses on the recognition and interpretation of hand gestures within sign language. This comprehensive solution utilizes the YOLOv5 object detection model to effectively identify common sign language expressions like "Hello," "I love you," "Yes," "No," and "Please." By doing so, it aims to enhance communication and foster a deeper understanding between individuals who use sign language and those who may not be familiar with it.

## Model Architecture
The project utilizes the YOLOv5 object detection model, a popular and efficient deep learning model for real-time object detection.
[Visit  YOLOv5 Github Repo](https://github.com/ultralytics/yolov5)

## Dataset Creation
To make YOLOv5 work, we need to teach it what the sign gestures look like. We do this by creating our own dataset and also integrating it with the publicly available datasets. For creating our own dataset, ran this code in Python.
 ```
import os
import cv2
import time
import uuid

IMAGE_PATH='CollectedImages'
labels=['Hello','Yes','No','Thanks']
number_of_images=4
for label in labels:
    img_path = os.path.join(IMAGE_PATH, label)
    os.makedirs(img_path)
    cap=cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(number_of_images):
        ret,frame=cap.read()
        imagename=os.path.join(IMAGE_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename,frame)
        cv2.imshow('frame',frame)
        time.sleep(2)
        
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    cap.release()
```
## Formatting Data

After Collecting  Data we have to format this image Yolo format  using online tools 
[Visit online tools link for formatting image](https://www.makesense.ai)

```
├───data
    ├───train
        ├───images
        ├───labels
```