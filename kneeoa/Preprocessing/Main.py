import sys
import cv2
import numpy as np
from preprocessing import Preprocess

print(sys.argv[1])

img = cv2.imread('uploads/'+sys.argv[1],0)
if img is None:
    print("Error: Image Doesn't Exist")
    exit()

#grayScale->roi->edgeDetection->contour
img_pre = Preprocess(img)    #this is a numpy Array
#work from here
name = sys.argv[1][:len(sys.argv[1])-4]+"p.jpg"
cv2.imwrite('uploads/prep/'+name,img_pre)
