#!/usr/bin/env python
# coding: utf-8

import requests


# url = "http://127.0.0.1:9696/predict"
url = "http://0.0.0.0:9696/predict"

client = {"job": "management", "duration": 400, "poutcome": "success"}

response = requests.post(url, json=client).json()
print(response)
