## subscription app
```
docker pull svizor/zoomcamp-model:3.11.5-hw10

docker run -it --rm -p 9696:9696 svizor/zoomcamp-model:3.11.5-hw10
```
python q6_test.py

----------------
## kind cluster

kind create cluster
kubectl cluster-info --context kind-kind

kubectl get service

----

kind load docker-image svizor/zoomcamp-model:3.11.5-hw10
kubectl apply -f deployment.yaml
kubectl get pod
kubectl describe pod <pod-name>

----

kubectl apply -f service.yaml
kubectl get service
kubectl port-forward service/<Service name> 9696:80

python q6_test.py
----


kubectl autoscale deployment subscription --name subscription-hpa --cpu-percent=20 --min=1 --max=3

kubectl get hpa

kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

kubectl get hpa subscription-hpa --watch

Update q6_test.py:
```
while True:
    sleep(0.1)
    response = requests.post(url, json=client).json()
    print(response)
```
python q6_test.py

----

kubectl delete deployment --all --namespace=default
kubectl delete service --all --namespace=default
