## ping app
```
pipenv install flask gunicorn

docker build -t ping:v001 .
docker run -it --rm -p 9696:9696 ping:v001
```
curl localhost:9696/ping

----------------
## kind cluster

kind create cluster
kubectl cluster-info --context kind-kind

kubectl get service

----

kubectl apply -f deployment.yaml
kind load docker-image ping:v001
kubectl get pod
kubectl describe pod <pod-name>
kubectl port-forward <pod-name> 9696:9696

curl localhost:9696/ping
----

kubectl apply -f service.yaml
kubectl get service
kubectl port-forward service/ping 8080:80

curl localhost:8080/ping
----

