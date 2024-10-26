#!/usr/bin/env python
# coding: utf-8

import pickle
from flask import Flask
from flask import jsonify
from flask import request

# model_file = "model1.bin"
model_file = "model2.bin"  # updated for homework Question6
dv_file = "dv.bin"

with open(model_file, "rb") as f_in:
    model = pickle.load(f_in)

with open(dv_file, "rb") as f_in:
    dv = pickle.load(f_in)

app = Flask("subscription-scoring-service")

@app.route("/predict", methods=["POST"])
def predict():
    client = request.get_json()

    X = dv.transform([client])
    score = model.predict_proba(X)[0, 1]
    score = {"subscription_probability": round(float(score), 3)}
    return jsonify(score)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)
