## Creating virtual env (for python dependency management)
```
pip install pipenv

pipenv install pandas numpy scikit-learn=0.24.2 flask gunicorn requests
```

This creates 2 files: `Pipfile` and `Pipfile.lock`.
To recreate virtual env on another system, just copy these 2 files there and run:
```
pipenv install
```
## --------------------------------------

- Running flask app via gunicorn
```
pipenv shell
gunicorn --bind 0.0.0.0:9696 predict:app
```
OR

```
pipenv run gunicorn --bind 0.0.0.0:9696 predict:app
```

- Testing From another terminal, run:
```
pipenv run python predict-test.py
pipenv run python predict-request-test.py
```

## --------------------------------------

- Testing/playing with docker image
```
docker run -it --rm python:3.8.12-slim
docker run -it --rm --entrypoint=bash python:3.8.12-slim
```

## Build docker image (for system dependency management)

- Create Dockerfile
- build docker image
- run docker image
```
docker build -t zoomcamp-test .
docker images
docker run -it --rm -p 9696:9696 zoomcamp-test
```

- Test from another terminal
```
python predict-request-test.py
```

## ----------------------------------------