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

def EdgeDetection(original_image):
    processed_img = original_image
    processed_img = cv2.GaussianBlur(processed_img, (3, 3), 7)
    processed_img = cv2.Canny(processed_img, threshold1=70, threshold2=150)
    #edges
    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180, 20, 15)
    draw_lines(processed_img, lines)
    return processed_img

def ApplyContour(img):
    ret, thresh = cv2.threshold(img, 100, 255, 0)
    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    img = np.dstack((img, img, img))
    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
    return img

def Roi(img):
    #         y1:y2    x1:x2
    img = img[250:500, 90:450]
    return img

def Preprocess(img):
    img_roi = Roi(img)
    img_edge = EdgeDetection(img_roi)
    final_img = ApplyContour(img_edge)
    #cv2.imshow('final_img', final_img)
    return final_img
