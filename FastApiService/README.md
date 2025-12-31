# FastAPI Service

A simple FastAPI microservice that provides REST API endpoints and can communicate with a Java Spring Boot service.

## 📋 Overview

This FastAPI service exposes multiple endpoints:
- **`/hello`** - Returns a greeting message
- **`/call-java`** - Calls the Java Spring Boot service and returns its response
- **`/health`** - Health check endpoint for monitoring

## 🔧 Requirements

### Local Development
- Python 3.9+
- pip (Python package manager)

### Runtime Dependencies
- FastAPI 0.104.1
- Uvicorn 0.24.0
- Requests 2.31.0
- Python-dotenv 1.0.0

### Docker & Kubernetes
- Docker (for building container images)
- kubectl (for Kubernetes deployment)
- Minikube (local Kubernetes cluster)

## 📦 Installation

### Step 1: Clone or Navigate to the Project
```bash
cd FastApiService
```

### Step 2: Create a Virtual Environment (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

## ▶️ Running the Application

### Local Development
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Or using Python directly:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

### Interactive API Documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🐳 Docker Setup

### Build Docker Image
```bash
docker build -t fastapi-service:latest .
```

### Run Docker Container
```bash
docker run -p 8000:8000 \
  -e SPRING_SERVICE_URL=http://spring-service:8080 \
  fastapi-service:latest
```

### Docker Compose (Optional)
If you have a `docker-compose.yml` file:
```bash
docker-compose up -d
```

## ☸️ Kubernetes Deployment

### Prerequisites
- Minikube running and accessible
- kubectl configured

### Deploy to Minikube
```bash
kubectl apply -f k8s-deployment.yaml  # if available
```

Or manually:
```bash
kubectl create deployment fastapi-service --image=fastapi-service:latest
kubectl expose deployment fastapi-service --port=8000 --type=LoadBalancer
```

### Port Forward to Access Service
```bash
kubectl port-forward service/fastapi-service 8000:8000
```

## 📝 API Endpoints

### 1. Hello Endpoint
**GET** `/hello`

Returns a greeting message from FastAPI.

**Response:**
```json
{
  "message": "Hello from FastAPI"
}
```

### 2. Call Java Service Endpoint
**GET** `/call-java`

Calls the Java Spring Boot service and returns its response.

**Response (Success):**
```json
{
  "from_java": {
    "message": "Hello from Spring Boot"
  }
}
```

**Response (Error):**
```json
{
  "error": "Failed to reach Spring service at http://spring-service:8080",
  "details": "Connection refused"
}
```

### 3. Health Check Endpoint
**GET** `/health`

Returns the health status of the service.

**Response:**
```json
{
  "status": "healthy"
}
```

## 🌍 Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `SPRING_SERVICE_URL` | `http://spring-service:8080` | URL of the Java Spring Boot service |

### Setting Environment Variables

**Locally:**
```bash
export SPRING_SERVICE_URL=http://localhost:8080
python main.py
```

**Docker:**
```bash
docker run -e SPRING_SERVICE_URL=http://spring-service:8080 fastapi-service:latest
```

**Kubernetes:**
Create a ConfigMap or update the deployment with environment variables:
```bash
kubectl set env deployment/fastapi-service SPRING_SERVICE_URL=http://spring-service:8080
```

## 🧪 Testing

### Using curl
```bash
# Test hello endpoint
curl http://localhost:8000/hello

# Test call-java endpoint
curl http://localhost:8000/call-java

# Test health endpoint
curl http://localhost:8000/health
```

### Using Python
```python
import requests

# Test endpoints
response = requests.get("http://localhost:8000/hello")
print(response.json())

response = requests.get("http://localhost:8000/call-java")
print(response.json())
```

## 📂 Project Structure
```
FastApiService/
├── main.py                 # FastAPI application code
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker container configuration
├── .gitignore            # Git ignore file
└── README.md             # This file
```

## 🔌 Integration with Spring Boot Service

This FastAPI service is designed to work with a Java Spring Boot service. To enable the `/call-java` endpoint:

1. Ensure the Spring Boot service is running on the configured `SPRING_SERVICE_URL`
2. The Spring Boot service should have a `/hello` endpoint that returns JSON
3. Call the `/call-java` endpoint from this service to get the response

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Find and kill the process using port 8000
lsof -i :8000
kill -9 <PID>
```

### Spring Service Unreachable
- Verify Spring service URL is correct
- Check if Spring service is running
- Verify network connectivity between services

### Import Errors
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

## 📜 License
See LICENSE file for details.

## 🤝 Contributing
Feel free to submit issues and enhancement requests!

## 📧 Support
For issues or questions, please contact the development team.
