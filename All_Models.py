import numpy as np 
import pandas as pd
import keras
import tensorflow as tf

from keras.models import Sequential
from keras.optimizers import Adam
from keras.losses import categorical_crossentropy
from keras.layers import Dense, Flatten, Conv3D, MaxPooling3D, DropoutDense, Flatten, Conv2D, MaxPooling2D, Dropout,GlobalAveragePooling2D,BatchNormalization
from sklearn.model_selection import train_test_split
'''These are models that were used to experiment and these were run on sample dataset.These models are originally done on Cifar-10 Dataset and used for classification purpose.
Lack of Regularization was the most important factor that observed through these models. Also some changes are also made in layers so as to adjust to our dataset.'''
'''Takes the Input Shape(inputShape as parameter is passed) and returns the model trained over dataset'''
def ConvPool_CNN_C(inputShape):
  model = Sequential()
  model.add(Conv2D(96,kernel_size=(3,3),activation='relu',padding='same'))
  model.add(Conv2D(96,kernel_size=(3,3),activation='relu',padding='same'))
  model.add(Conv2D(96,kernel_size=(3,3),activation='relu',padding='same'))
  model.add(MaxPooling2D(pool_size=(3,3),strides=2))
  model.add(Conv2D(192,(3,3),activation='relu',padding='same'))
  model.add(Conv2D(192,(3,3),activation='relu',padding='same'))
  model.add(Conv2D(192,(3,3),activation='relu',padding='same'))
  model.add(MaxPooling2D(pool_size=(3,3),strides=2))
  model.add(Conv2D(192,(3,3),activation='relu',padding='same'))
  model.add(Conv2D(192,(1,1),activation='relu'))
  model.add(Conv2D(5,(1,1)))
  model.add(GlobalAveragePooling2D())
  model.add(Flatten())
  model.add(Dense(5, activation='softmax'))
  model.build(inputShape)
  model.compile(loss=categorical_crossentropy,optimizer=keras.optimizers.Adam(0.001),metrics=['accuracy'])
  return model

def all_cnn_c(inputShape):
  model = Sequential()
  model.add(Conv2D(96,kernel_size=(3,3),activation='relu',padding='same'))
  model.add(Conv2D(96,kernel_size=(3,3),activation='relu',padding='same'))
  model.add(Conv2D(96,kernel_size=(3,3),activation='relu',padding='same'))
  model.add(Conv2D(192,(3,3),activation='relu',padding='same'))
  model.add(Conv2D(192,(3,3),activation='relu',padding='same'))
  model.add(Conv2D(192,(3,3),activation='relu',padding='same'))
  model.add(Conv2D(192,(3,3),activation='relu',padding='same'))
  model.add(Conv2D(192,(1,1),activation='relu'))
  model.add(GlobalAveragePooling2D())
  model.add(Dense(5, activation='softmax'))
  model.build(inputShape)
  model.compile(loss=categorical_crossentropy,optimizer=Adam(0.001),metrics=['accuracy'])

  return model

def nin_cnn_c(inputShape):
  model = Sequential()
  model.add(Conv2D(32,kernel_size=(5,5),activation='relu',padding='valid'))
  model.add(Conv2D(32,kernel_size=(5,5),activation='relu'))
  model.add(Conv2D(32,kernel_size=(5,5),activation='relu'))
  model.add(MaxPooling2D(pool_size=(3,3),strides=2))
  model.add(Dropout(0.5))
  model.add(Conv2D(64,(3,3),activation='relu',padding='same'))
  model.add(Conv2D(64,(1,1),activation='relu',padding='same'))
  model.add(Conv2D(64,(1,1),activation='relu',padding='same'))
  model.add(MaxPooling2D(pool_size=(3,3),strides=2))
  model.add(Dropout(0.5))
  model.add(Conv2D(128,(3,3),activation='relu',padding='same'))
  model.add(Conv2D(32,(1,1),activation='relu'))
  model.add(Conv2D(5,(1,1)))
  model.add(GlobalAveragePooling2D())
  model.add(Flatten())
  model.add(Dense(5, activation='softmax'))
  model.build(inputShape)
  
  model.compile(loss=categorical_crossentropy,optimizer=Adam(0.001),metrics=['accuracy'])
  return model

def SimpleModel(inputShape):
	model = tf.keras.models.Sequential([
    keras.layers.Dense(512, activation='relu', input_shape = inputShape),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10)
    ])

	model.compile(optimizer='adam',
                loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=[tf.metrics.SparseCategoricalAccuracy()])

	return model
