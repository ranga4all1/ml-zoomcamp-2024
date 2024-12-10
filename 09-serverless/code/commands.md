```
conda create -n ml-zoomcamp python=3.10 numpy jupyter matplotlib
conda activate ml-zoomcamp
pip install tensorflow
```

```
docker build -t clothing-model .
docker run -it --rm -p 8080:8080 clothing-model:latest
```

