import cv2
import glob, os
import numpy as np
import pandas as pd
from preprocessing import Preprocess

df = []
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
        df.append([img_CLAHE,grade+1])

df = pd.DataFrame(df,columns = ['Image','Grade'])
#shuffle
df = df.sample(frac = 1)

#df has two coloumns Image and Grade-> split it(70,30) and apply model
#don't paste the code directly rather make a different .py file and use functions

'''
#testing Code
img = cv2.imread("2.png")
if img is None:
    print("Error: Image Doesn't Exist")
    exit()

#grayScale->roi->edgeDetection->contour
img1 = np.array(img, dtype=np.uint8)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img_pre,img_CLAHE = Preprocess(img1)    #this is a numpy Array
#work from here 
cv2.imwrite("2_preprocessed.jpg", img_pre)
cv2.imwrite("2_CLAHE.jpg", img_CLAHE)
'''