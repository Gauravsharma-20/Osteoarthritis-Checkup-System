import cv2
import numpy as np

def applyContour(img):
    ret, thresh = cv2.threshold(img, 100, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    img = np.dstack((img, img, img))
    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
    return img

def roi(img):
    #         x1:x2    y1:y2
    img = img[250:450,100:400]
    return img

#read GrayScale image
img = cv2.imread("1_low.jpg", 0)
img = roi(img)
final_img = applyContour(img)
#cv2.imshow('final_img', final_img)
cv2.imwrite("1_low_contour.jpg", final_img)
