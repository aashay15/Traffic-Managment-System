import numpy as np
import cv2
names = ['vid2.MOV', 'vid3.MOV', 'vid4.MOV']
img_array =[]
def multi_images():
    for i in names:
        cap = cv2.VideoCapture(i) #video_name is the video being called
        cap.set(1,1); # Where frame_no is the frame you want
        ret, frame = cap.read() # Read the frame
        #img_array.append(frame)
        #cv2.imshow('window_name', frame) # show frame on window
        cv2.imwrite('frame{}.jpg'.format(i),frame)
        img_array.append('frame{}.jpg'.format(i))
    return img_array

IMAGE_NAME = multi_images()
print(IMAGE_NAME)

