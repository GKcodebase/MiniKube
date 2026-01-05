# **MiniKube — Local demo repository**

- **Description:**: Multi-service demo repository containing a Python FastAPI service, a Java Spring Boot service, Kubernetes manifests, and an embedded Istio distribution for local experimentation.
- **Contents:**: FastAPI, SpringBoot, Kubernetes manifests, and Istio files for local cluster testing.

## **Components**
- **FastAPI Service:**: See [FastApiService/main.py](FastApiService/main.py) — simple FastAPI app exposing `/hello`, `/call-java` and `/health` on port `8000`.
- **Spring Boot Service:**: See [SpringBootService/README.md](SpringBootService/README.md) and [SpringBootService/pom.xml](SpringBootService/pom.xml) — Java service exposing `/hello` and `actuator/health` on port `8080`.
- **Kubernetes Manifests:**: See [KubernetesService](KubernetesService) — `fastapi-deployment.yaml`, `fastapi-service.yaml`, `spring-deployment.yaml`, `spring-service.yaml` (images referenced: `fastapi-app:1.0`, `spring-app:1.0`).
- **Istio Distribution:**: Local Istio manifests and `istioctl` live under [istio-1.28.2](istio-1.28.2). Use the bundled `istioctl` to install or manage Istio in the cluster.

## **Prerequisites**
- **Local tools:**: `docker`, `kubectl`, `minikube` (or a local k8s cluster), `java` (17+), `mvn`, `python3` (3.8+), `pip`.
- **Optional:**: Use `istioctl` from [istio-1.28.2/bin/istioctl](istio-1.28.2/bin/istioctl) for Istio installation and management.

## **Quickstart — Minikube (recommended for local)**
- Start Minikube:

```bash
minikube start --driver=docker
```

- Option A — build Docker images into Minikube's Docker daemon:

```bash
# Use Minikube's Docker daemon in your shell
eval "$(minikube -p minikube docker-env)"
# Build images with tags referenced in manifests
docker build -t fastapi-app:1.0 FastApiService
docker build -t spring-app:1.0 SpringBootService
```

- Option B — build images locally and load into Minikube:

```bash
docker build -t fastapi-app:1.0 FastApiService
docker build -t spring-app:1.0 SpringBootService
minikube image load fastapi-app:1.0
minikube image load spring-app:1.0
```

- Deploy Kubernetes manifests:

```bash
kubectl apply -f KubernetesService/fastapi-deployment.yaml
kubectl apply -f KubernetesService/fastapi-service.yaml
kubectl apply -f KubernetesService/spring-deployment.yaml
kubectl apply -f KubernetesService/spring-service.yaml
```

- Verify pods and services:

```bash
kubectl get pods
kubectl get svc
```

- Access FastAPI via port-forward (example):

```bash
kubectl port-forward service/fastapi-service 8080:80
# FastAPI reachable at http://localhost:8080/hello
curl http://localhost:8080/hello
```

- Access Spring Boot via port-forward (example):

```bash
kubectl port-forward service/spring-service 8080:8080
curl http://localhost:8080/hello
curl http://localhost:8080/actuator/health
```

**Local development**
- FastAPI (run locally):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r FastApiService/requirements.txt
python FastApiService/main.py
# Open http://localhost:8000/hello
```

- Spring Boot (run locally):

```bash
cd SpringBootService
mvn clean package
java -jar target/spring-boot-service-1.0.0.jar
# Open http://localhost:8080/hello
```

## **Istio notes (local experimentation)**
- The repo includes `istio-1.28.2`. You can use the bundled `istioctl` to install Istio into Minikube:

```bash
# Example: install demo profile (not for production)
./istio-1.28.2/bin/istioctl install --set profile=demo -y
# Enable automatic sidecar injection for namespace
kubectl label namespace default istio-injection=enabled --overwrite
```

- After installing Istio, you can apply Kubernetes manifests and observe traffic routing, telemetry, and mTLS behavior. See `istio-1.28.2/README.md` for more details.

## **Images and manifest mapping**
- Kubernetes manifests expect these image tags:
  - `fastapi-app:1.0` — built from `FastApiService/Dockerfile` (ensure it exposes port 8000)
  - `spring-app:1.0` — built from `SpringBootService/Dockerfile` (exposes port 8080)

## **Service endpoints & behavior**
- FastAPI endpoints (default port 8000):
  - `/hello` — returns a greeting
  - `/call-java` — calls `spring-service:8080/hello` inside k8s cluster
  - `/health` — health check
- Spring Boot endpoints (default port 8080):
  - `/hello` — greeting
  - `/actuator/health` — actuator health

## **Troubleshooting & tips**
- If `kubectl` shows ImagePullBackOff, ensure images are available to the cluster (use `minikube image load` or build inside minikube docker-env).
- To inspect logs:

```bash
kubectl logs deployment/fastapi -f
kubectl logs deployment/spring -f
```

- If ports conflict locally, use `kubectl port-forward` to map to different local ports.

## **Useful files**
- [FastApiService/main.py](FastApiService/main.py)
- [FastApiService/requirements.txt](FastApiService/requirements.txt)
- [SpringBootService/Dockerfile](SpringBootService/Dockerfile)
- [SpringBootService/pom.xml](SpringBootService/pom.xml)
- [KubernetesService](KubernetesService)
- [istio-1.28.2](istio-1.28.2)

**License**
See the repository `LICENSE` file.

---
