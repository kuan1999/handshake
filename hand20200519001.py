#count shrump test1 for fir
from skimage import data
from skimage import io,color
import skimage.morphology as sm
import matplotlib.pyplot as plt
import numpy as np
import cv2
import copy
cap = cv2.VideoCapture('/Users/hykuan/Documents/GSLab/hand/hand1.mp4',0)
#kernel = np.ones((2,2),np.uint64)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('IIR01.AVI', fourcc, 20.0, (640, 480))    
ret,frame = cap.read()

new_img=frame.copy()
gray_new = cv2.cvtColor( new_img, cv2.COLOR_BGR2GRAY)
gray_old = gray_new.copy()

while(cap.isOpened()):
    
    if ret == True:
        new_img = frame.copy()
        gray_new = cv2.cvtColor( new_img, cv2.COLOR_BGR2GRAY)
        gray_old = gray_old*0.6+gray_new*0.4
        print(type(gray_old[0,0]))
        int_32_gray = np.array( gray_old, dtype = np.uint8 ) 
        result = cv2.absdiff(gray_new,int_32_gray)
        out.write(frame)
        cv2.imshow('frame',result)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        ret,frame = cap.read()
    else:
        break   

cap.release()
out.release()
cv2.destroyAllWindows()