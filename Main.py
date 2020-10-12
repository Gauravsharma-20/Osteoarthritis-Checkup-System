import cv2
import glob, os
import numpy as np
import pandas as pd
import tensorflow as tf
from preprocessing import Preprocess
import Model
from matplotlib import pyplot as plt

df_train = []
df_test = []
df_val = []

if os.path.exists("./dataset/train.npy"):
    df_train = np.load("./dataset/train.npy")
    df_test = np.load("./dataset/test.npy")
    df_val = np.load("./dataset/val.npy")
else:
    #TRAIN
    for grade in range(5):
        images=[ cv2.imread(file) for file in glob.glob(r'C:/Users/Gaurav/Desktop/Minor_Project/MinorProject/dataset/train/'+str(grade)+'/*.png')]
        path_input = r'C:/Users/Gaurav/Desktop/Minor_Project/MinorProject/dataset/train/'+str(grade)
        fnames = os.listdir(path_input)
        for f in fnames:
            img = cv2.imread(os.path.join(path_input,f),0)
            #img = images[i]
            #i += 1
            img1 = np.array(img, dtype=np.uint8)
            img_pre,img_CLAHE = Preprocess(img1)
            med= cv2.medianBlur(img_CLAHE, 3)
            w= os.path.split(f)[1].split('.')[0]
            if (w.find('L') != -1):
                cv2.imwrite(r'C:/Users/Gaurav/Desktop/Minor_Project/MinorProject/dataset/train/'+str(grade)+'/'+w+'.png', np.fliplr(med))
            else:
                cv2.imwrite(r'C:/Users/Gaurav/Desktop/Minor_Project/MinorProject/dataset/train/'+str(grade)+'/'+w+'.png', med)
            
            #img_pre:grayScale->roi->CLAHE->edgeDetection->contour
            #img_CLAHE:grayScale->CLAHE
            img_CLAHE = img_CLAHE/255.0
            df_train.append([img_CLAHE,grade+1])
    #TEST
    for grade in range(5):
        images=[ cv2.imread(file) for file in glob.glob(r'C:/Users/Gaurav/Desktop/Minor_Project/MinorProject/dataset/test/'+str(grade)+'/*.png')]
        for img in images:
            img1 = np.array(img, dtype=np.uint8)/255.0
            df_test.append([img1,grade+1])
    #VAL
    for grade in range(5):
        images=[ cv2.imread(file) for file in glob.glob(r'C:/Users/Gaurav/Desktop/Minor_Project/MinorProject/dataset/val/'+str(grade)+'/*.png')]
        for img in images:
            img1 = np.array(img, dtype=np.uint8)/255.0
            df_test.append([img1,grade+1])
    np.save('train.npy',df_train)
    np.save('test.npy',df_test)
    np.save('val.npy',df_val)
    
print("*****Loading Done!*****")
'''
#shuffle
df_train = df_train.sample(frac = 1)
X_train, Y_train = df_train['Image'], df_train['Grade']
X_test, Y_test = df_test['Image'], df_test['Grade']
X_val, Y_val = df_val['Image'], df_val['Grade']
print("Splitting Done!")
#df has two coloumns Image and Grade
#don't paste the code directly rather make a different .py file and use functions

model_1 = Model.ConvPoolModel(inputShape)
history_1 = model_1.fit(X_train, Y_train,batch_size=32,epochs = 5,verbose = 1)

model_2 = Model.SimpleModel(inputShape)
filepath = 'Simple_Model.hdf5'
checkpoint = tf.keras.callbacks.ModelCheckpoint(filepath, monitor='val_loss', verbose=1, save_best_only=True,mode='auto', save_frequency=1)
history_2 = model_2.fit(X_train, Y_train,batch_size = 32,epochs = 5,verbose = 1,validation_split = 0.2,validation_data = (X_val, Y_val),callbacks = [checkpoint],shuffle=True)
'''
print("DONE")