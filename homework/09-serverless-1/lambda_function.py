#!/usr/bin/env python
# coding: utf-8

import urllib.request as request
from io import BytesIO
import numpy as np
from PIL import Image
import tflite_runtime.interpreter as tflite

# Load the TFLite model
interpreter = tflite.Interpreter(model_path='model_2024_hairstyle.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']


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

def preprocess_input(x):
    # Convert to float first
    x = x.astype('float32')  # or 'float64'
    x /= 255.
    return x

# Define the classes
classes = ['curly',
           'straight']

# url = "https://habrastorage.org/webt/yf/_d/ok/yf_dokzqy3vcritme8ggnzqlvwa.jpeg"
target_size = (200, 200)


def predict(url):
    # Download and prepare the image
    img = download_image(url)
    img = prepare_image(img, target_size)

    # Preprocess the image
    x = np.array(img)
    X = np.array([x])
    X = preprocess_input(X)

    # Make the prediction
    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    # Extract probabilities
    float_predictions = preds[0].tolist()
    curly_probability = float_predictions[0]
    straight_probability = 1.0 - curly_probability

    # Return probabilities and binary decision
    return {
        'curly_probability': curly_probability,
        'straight_probability': straight_probability,
        'is_curly': curly_probability > 0.5  # True if curly, False otherwise
    }

def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result