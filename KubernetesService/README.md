# Kubernetes Service Manifests

This folder contains Kubernetes manifests for two example services used in this workspace:

- `fastapi-deployment.yaml` — FastAPI deployment + service
- `fastapi-service.yaml` — Service manifest for the FastAPI app
- `spring-deployment.yaml` — Spring Boot deployment
- `spring-service.yaml` — Service manifest for the Spring Boot app

## Prerequisites

- A running Kubernetes cluster (minikube, kind, or remote cluster)
- `kubectl` configured to talk to your cluster

## Apply the manifests

Apply all manifests in this folder:

```bash
kubectl apply -f KubernetesService/
```

Or apply files individually:

```bash
kubectl apply -f KubernetesService/fastapi-deployment.yaml
kubectl apply -f KubernetesService/fastapi-service.yaml
kubectl apply -f KubernetesService/spring-deployment.yaml
kubectl apply -f KubernetesService/spring-service.yaml
```

## Common kubectl commands

- List resources (pods, services, deployments):

```bash
kubectl get pods
kubectl get svc
kubectl get deployments
kubectl get all
```

- Describe a resource for details and events:

```bash
kubectl describe pod <pod-name>
kubectl describe svc <service-name>
kubectl describe deployment <deployment-name>
```

- View logs (follow):

```bash
kubectl logs -f deployment/<deployment-name>
# or for a specific pod
kubectl logs -f <pod-name>
```

- Exec into a running pod (interactive shell):

```bash
kubectl exec -it <pod-name> -- /bin/sh
# or bash if available
kubectl exec -it <pod-name> -- /bin/bash
```

- Port-forward to access a service or pod locally:

```bash
# Forward deployment port (example: local 8000 -> pod 8000)
kubectl port-forward deployment/<deployment-name> 8000:8000

# Forward a specific pod port
kubectl port-forward pod/<pod-name> 8080:8080
```

- Scale a deployment:

```bash
kubectl scale deployment/<deployment-name> --replicas=3
```

- Rolling update / restart and status:

```bash
kubectl rollout status deployment/<deployment-name>
kubectl rollout restart deployment/<deployment-name>
kubectl rollout history deployment/<deployment-name>
```

- Update image for a deployment:

```bash
kubectl set image deployment/<deployment-name> <container-name>=myimage:tag
```

- Delete resources (cleanup):

```bash
kubectl delete -f KubernetesService/
# or delete by resource
kubectl delete deployment <deployment-name>
kubectl delete svc <service-name>
```

## Examples using the provided manifests

- Apply FastAPI manifests and check pods:

```bash
kubectl apply -f KubernetesService/fastapi-deployment.yaml
kubectl apply -f KubernetesService/fastapi-service.yaml
kubectl get pods -l app=fastapi
kubectl get svc fastapi
```

- Port-forward FastAPI locally (adjust ports to match manifest):

```bash
kubectl port-forward svc/fastapi 8000:80
# Then open http://localhost:8000
```

## Tips

- Use `kubectl get all -o wide` for extra columns and node info.
- Use `-n <namespace>` to operate in a specific namespace.
- Use `kubectl apply -f` to make manifests declarative and idempotent.

If you want, I can also add a brief CI/deploy example or create a Helm chart for these manifests. 
