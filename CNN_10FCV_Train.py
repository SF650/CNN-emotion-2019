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
os.environ["PATH"] += os.pathsep +'C:/Program Files (x86)/Graphviz2.38/bin/'

sess = tf.Session(config=tf.ConfigProto(device_count={'gpu':0}))

# this is the augmentation configuration we will use for training
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
valid_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

cvscores = []

for i in range(1,11):
    
    print("Iteration " + str(i) + ":\n===============================")
    
    model = Sequential()
    model.add(Convolution2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)))
    model.add(Convolution2D(32, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2) ,data_format="channels_last"))
    model.add(Dropout(0.25))

    model.add(Convolution2D(64, (3, 3), activation='relu'))
    model.add(Convolution2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2), data_format="channels_last"))
    model.add(Dropout(0.25))

    model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(21))
    model.add(Activation('sigmoid'))

    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy', acc_top3])
    
    train_generator = train_datagen.flow_from_directory(
        '../10CrossFolderValidation/' + str(i) + '/train',
        target_size=(64, 64),
        batch_size=128,
        class_mode='categorical')
    
    validation_generator = valid_datagen.flow_from_directory(
        '../10CrossFolderValidation/' + str(i) + '/validation',
        target_size=(64, 64),
        batch_size=128,
        class_mode='categorical')
    
    test_generator = test_datagen.flow_from_directory(
        '../10CrossFolderValidation/' + str(i) + '/test',
        target_size=(64, 64),
        batch_size=128,
        class_mode='categorical')
    
    tStart = time.time()
    
    train_history = model.fit_generator(
        train_generator,
        validation_data=validation_generator,
        verbose=1,
        steps_per_epoch=400,
        epochs=100,
        validation_steps=16,
        workers=2
        )

    tEnd = time.time()
    print("Iteration " + str(i) + " - cost " + str(tEnd - tStart) + " sec")
    
    scores = model.evaluate_generator(test_generator, steps=test_generator.batch_size)
    print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
    cvscores.append(scores[1] * 100)

print("%.2f%% (+/- %.2f%%)" % (np.mean(cvscores), np.std(cvscores)))

#save model
model.save('CNN_10FCV_CQT_Final.h5')