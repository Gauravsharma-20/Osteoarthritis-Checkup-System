
import cv2, time 
import numpy as np

img = cv2.imread("Different_images/9048979L_NEW.png",0)
img = np.array(img,dtype=np.uint8)
processed_img = cv2.Canny(img, threshold1=125, threshold2=190)
cv2.imwrite("Different_images/9048979L_Edge.png",processed_img)

