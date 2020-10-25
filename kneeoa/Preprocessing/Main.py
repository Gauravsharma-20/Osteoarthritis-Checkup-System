import sys
import numpy as np
import cv2
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense, Flatten, BatchNormalization, Conv2D, MaxPool2D
from tensorflow.keras.layers import Dropout
from keras import regularizers
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model

def preprocess(img):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img,(224,224))
    img = np.array(img,dtype=np.uint8)
    img = cv2.GaussianBlur(img, (3, 3), 7)
    mean = int(np.mean(img))
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            img[i,j] = max(0,img[i,j]-mean)
    clahe = cv2.createCLAHE()
    img = clahe.apply(img)
    img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    img = img.reshape(-1, 224, 224, 3)
    return img

#Enter File locaion here
file_loc = "uploads/"+sys.argv[1]
img = cv2.imread(file_loc)
pre_img = preprocess(img)
scaled_img = pre_img/255.0

model = load_model("Extensive_Model.h5")
predicted_grade = model.predict(scaled_img,verbose=0)
predicted_grade = np.argmax(predicted_grade,axis=-1)

#save preprocessed image for output
#cv2.imwrite('output_location',pre_img)
print("Grade :",predicted_grade) 