import constants.constants as CONST
import matplotlib.pyplot as plt 
import os
import pickle
import tensorflow as tf
from tensorflow.keras.utils import Sequence
from tensorflow.keras.optimizers import Adam, SGD
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras import models, layers, optimizers
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.layers import Dense, Dropout, Flatten, MaxPooling1D, Conv1D


def get_model():
    model = Sequential()
    model.add(Conv1D(filters =196, kernel_size=19, strides=3, activation='relu', 
                     input_shape=(CONST.SEQ_SIZE,CONST.LEN_SIZE)))
    model.add(MaxPooling1D(pool_size=5))

    model.add(Conv1D(filters =196, kernel_size=19, strides=3, activation='relu'))
    model.add(MaxPooling1D(pool_size=5))

    model.add(tf.keras.layers.Flatten())

    #Full Connection
    model.add(Dense(units = 164, activation = 'relu'))

    model.add(Dense(units = 42, activation = 'relu'))

    model.add(Dense(units = 20, activation = 'relu'))
    model.add(Dropout(0.40)) # update= more dropout .25 -> .40

    model.add(Dense(5, activation='softmax'))

    opt = Adam(learning_rate=0.0014924)
    model.compile(loss='categorical_crossentropy', optimizer= opt, 
                  metrics=['accuracy'])
    return model


def plotter(history, pickle_file=False):
    
    if pickle_file:
        with open(history, 'rb') as file:
            history = pickle.load(file)
    else:
        history = history.history
        
    plt.figure()
    plt.plot(history['accuracy'])
    plt.plot(history['val_accuracy'])
    plt.title('Model Accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'])
    plt.savefig(f"{CONST.RSLT_DIR}/Training_validation_accuracy.jpg")

    plt.figure()
    plt.plot(history['loss'])
    plt.plot(history['val_loss'])
    plt.title('Model Loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'])
    plt.savefig(f"{CONST.RSLT_DIR}/Training_validation_loss.jpg")