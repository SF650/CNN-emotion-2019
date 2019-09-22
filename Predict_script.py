import tensorflow as tf
import h5py
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from keras.callbacks import EarlyStopping
from keras.preprocessing.image import ImageDataGenerator
from keras.utils.vis_utils import plot_model
from keras.callbacks import TensorBoard
from sklearn.model_selection import KFold
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense

import time
import os

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        '../10CrossFolderValidation/10/train',
        target_size=(64, 64),
        batch_size=128,
        class_mode='categorical')


test_generator = test_datagen.flow_from_directory(
        '../10CrossFolderValidation/10/test', 
        target_size=(64, 64), 
        class_mode='categorical',
        shuffle=False) 

%matplotlib inline
from sklearn.metrics import classification_report, confusion_matrix

#Confution Matrix and Classification Report
Y_pred = model.predict_generator(test_generator)
y_pred = np.argmax(Y_pred, axis=1)

labels = (test_generator.class_indices)
labels = dict((v,k) for k,v in labels.items())
predictions = [labels[k] for k in y_pred]

CM = confusion_matrix(test_generator.classes, y_pred)
CMP = classification_report(test_generator.classes, y_pred)

print('Confusion Matrix')
print(CM)
print('Classification Report')
print(CMP)