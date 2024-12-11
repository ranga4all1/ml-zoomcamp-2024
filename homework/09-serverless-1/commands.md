```
conda create -n ml-zoomcamp python=3.10 numpy jupyter matplotlib
conda activate ml-zoomcamp
pip install tensorflow==2.17.1
pip install keras-image-helper
pip install numpy==1.23.1
pip install --no-deps https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl
```

```
docker build -t hairstyle-model .
docker run -it --rm -p 8080:8080 hairstyle-model:latest
```
