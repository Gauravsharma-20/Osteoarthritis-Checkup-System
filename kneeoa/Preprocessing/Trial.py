import cv2
import numpy as np
np.set_printoptions(threshold=np.inf)


def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    #print(v.head(5))
    print(sum(v))
    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img


img = cv2.imread('2.jpeg')  # load rgb image
img_final = increase_brightness(img, value=20)
#cv2.imshow('Original image',img)
#cv2.imshow('Final image', img_final)
cv2.imwrite("2_processed.jpg", img_final)
