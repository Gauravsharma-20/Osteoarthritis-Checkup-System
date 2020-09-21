import cv2
import numpy as np
from preprocessing import Preprocess


img = cv2.imread("1_low_bright.jpg", 0)
if img is None:
    print("Error: Image Doesn't Exist")
    exit()

#grayScale->roi->edgeDetection->contour
img_pre = Preprocess(img)    #this is a numpy Array
#work from here 
cv2.imwrite("1_low_preprocessed.jpg", img_pre)
