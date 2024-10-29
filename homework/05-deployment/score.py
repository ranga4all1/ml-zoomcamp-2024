#!/usr/bin/env python
# coding: utf-8

import pickle

client = {
    "job": "management",
    "duration": 400,
    "poutcome": "success"
    }

model_file = "model1.bin"
dv_file = "dv.bin"

with open(model_file, "rb") as f_in:
    model = pickle.load(f_in)

with open(dv_file, "rb") as f_in:
    dv = pickle.load(f_in)


X = dv.transform([client])
score = model.predict_proba(X)[0, 1]
print(f"Subscription probability: {score:.3f}")
