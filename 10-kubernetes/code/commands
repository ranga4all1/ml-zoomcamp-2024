```
pip install grpcio==1.42.0 tensorflow-serving-api==2.7.0
pip install keras-image-helper
```
## run the model (clothing-model) with the prebuilt docker image tensorflow/serving:2.7.0:
```
docker run -it --rm \
  -p 8500:8500 \
  -v $(pwd)/clothing-model:/models/clothing-model/1 \
  -e MODEL_NAME="clothing-model" \
  tensorflow/serving:2.7.0
```

pipenv install grpcio==1.42.0 flask gunicorn keras-image-helper
pipenv install tensorflow-protobuf==2.7.0 protobuf==3.19


docker build -t zoomcamp-10-model:xception-v4-001 \
  -f image-model.dockerfile .

docker run -it --rm \
  -p 8500:8500 \
  zoomcamp-10-model:xception-v4-001

docker build -t zoomcamp-10-gateway:002 \
  -f image-gateway.dockerfile .

docker run -it --rm \
  -p 9696:9696 \
  zoomcamp-10-gateway:001


docker-compose up

docker-compose up -d
docker-compose down

docker build -t ping:v001 .
docker run -it --rm -p 9696:9696 ping:v001