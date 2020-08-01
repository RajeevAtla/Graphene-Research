from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow import keras
from keras import layers, models


import glob
import imageio
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import PIL
import time
import functools
from IPython import display


#import data using pandas
data = pd.read_csv('dataset.csv', sep = ',', header = 0)
data.pop('material')
data.pop('critical_temp')

#print(data, data.dtypes) #sanity check

data_tensor = tf.data.Dataset.from_tensor_slices((data)).shuffle(100)


def make_generator():
    model = tf.keras.Sequential()
    model.add(layers.Dense(7*7*256, use_bias=False, input_shape=(100,)))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Reshape((7, 7, 256)))
    assert model.output_shape == (None, 7, 7, 256) # Note: None is the batch size

    model.add(layers.Conv2DTranspose(128, (5, 5), strides=(1, 1), padding='same', use_bias=False))
    assert model.output_shape == (None, 7, 7, 128)
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Conv2DTranspose(64, (5, 5), strides=(2, 2), padding='same', use_bias=False))
    assert model.output_shape == (None, 14, 14, 64)
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Conv2DTranspose(1, (5, 5), strides=(2, 2), padding='same', use_bias=False, activation='tanh'))
    assert model.output_shape == (None, 28, 28, 1)


    return model

def make_discriminator():
    model = tf.keras.Sequential

    model.add(layers.Dense(2, activation = "relu"))
    model.add(layers.Dense(3, activation = "relu"))
    model.add(layers.Dense(4))

    return model

discriminator = make_discriminator()
generator = make_generator()
