#!/usr/bin/env python
# coding: utf-8

import numpy as np
from io import BytesIO
from urllib import request

from PIL import Image

import tensorflow as tf
from tensorflow import keras
import tensorflow.lite as tflite

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import load_img

from tensorflow.keras.applications.xception import preprocess_input



model = keras.models.load_model('model_2024_hairstyle.keras')

converter = tf.lite.TFLiteConverter.from_keras_model(model)

tflite_model = converter.convert()

with open('model_2024_hairstyle.tflite', 'wb') as f_out:
    f_out.write(tflite_model)

# model size
!ls -lh


# index

interpreter = tflite.Interpreter(model_path='model_2024_hairstyle.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

print(f"output_index: {output_index}")


# Preparing the image

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img


url = "https://habrastorage.org/webt/yf/_d/ok/yf_dokzqy3vcritme8ggnzqlvwa.jpeg"
target_size = (200, 200)

img = download_image(url)
img = prepare_image(img, target_size)

x = np.array(img)
X = np.array([x])
X.shape

def preprocess_input(x):
    # Convert to float first
    x = x.astype('float32')  # or 'float64'
    x /= 255.
    return x

X = preprocess_input(X)

X[:0]

interpreter.set_tensor(input_index, X)
interpreter.invoke()
preds = interpreter.get_tensor(output_index)

