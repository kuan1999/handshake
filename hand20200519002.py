#count shrump test1 for fir
from skimage import data
from skimage import io,color
import skimage.morphology as sm
import matplotlib.pyplot as plt
import numpy as np
import cv2
import copy
#cap = cv2.VideoCapture('/Users/hykuan/Documents/GSLab/hand/hand1.mp4',0) 

cap = cv2.VideoCapture(0) 
ret,frame = cap.read()
t=0
new_img=frame.copy()

gray_new = cv2.cvtColor( new_img, cv2.COLOR_BGR2GRAY)
gray_old = gray_new.copy()
while(cap.isOpened()):
    
    if ret == True:
        if t== 0 :
            for i in range(50):
                new_img = frame.copy()
                gray_new = cv2.cvtColor( new_img, cv2.COLOR_BGR2GRAY)   
                gray_old = gray_old*0.9+gray_new*0.1
                int_32_gray = np.array( gray_old, dtype = np.uint8 ) 
                ret,frame = cap.read() 
                t=t+1
        ret,frame = cap.read()

        new=frame.copy()
        gray = cv2.cvtColor( new, cv2.COLOR_BGR2GRAY)
        medianblur1 = cv2.medianBlur(int_32_gray,31)
        medianblur2 = cv2.medianBlur(gray,31)
        result=cv2.absdiff(medianblur1 ,medianblur2)
        #cv2.subtract(int_32_gray,gray)
        ret, img2 = cv2.threshold(result, 50, 255, cv2.THRESH_BINARY)
        cv2.imshow('frame',img2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        ret,frame = cap.read()
    else:
        break   

cap.release()
cv2.destroyAllWindows()