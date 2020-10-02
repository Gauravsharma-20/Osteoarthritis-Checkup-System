import cv2
import numpy as np


def draw_lines(img, lines):
    try:
        for line in lines:
            coords = line[0]
            cv2.line(img, (coords[0], coords[1]),
                     (coords[2], coords[3]), [255, 255, 255], 3)
    except:
        pass


def edgeDetection(original_image):
    processed_img = original_image
    processed_img = cv2.GaussianBlur(processed_img, (3, 3), 7)
    processed_img = cv2.Canny(processed_img, threshold1=70, threshold2=150)
   
    #                   edges
    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180, 20, 15)
    draw_lines(processed_img, lines)
    return processed_img


img = cv2.imread('1_low_processed.jpg')
img_edge = edgeDetection(img)
cv2.imshow('Final image', img_edge)
cv2.imwrite("1_low_edge.jpg", img_edge)
