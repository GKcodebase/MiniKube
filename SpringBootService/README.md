# Spring Boot Service

A simple Spring Boot REST API microservice that provides greeting endpoints.

## 📋 Overview

This Spring Boot service exposes multiple REST endpoints:
- **`/hello`** - Returns a greeting message from Spring Boot
- **`/`** - Welcome endpoint with service information
- **`/info`** - Returns application and system information
- **`/actuator/health`** - Health check endpoint for monitoring

## 🔧 Requirements

### Local Development
- Java 17 or higher
- Maven 3.6+ or Gradle 7.0+
- Maven (for building and running the application)

### Runtime Dependencies
- Spring Boot 3.2.1
- Spring Boot Starter Web
- Spring Boot Starter Actuator
- Lombok (optional, for reducing boilerplate)

### Docker & Kubernetes
- Docker (for building container images)
- kubectl (for Kubernetes deployment)
- Minikube (local Kubernetes cluster)

## 📦 Installation

### Step 1: Clone or Navigate to the Project
```bash
cd SpringBootService
```

### Step 2: Verify Java Installation
```bash
java -version
# Output should show Java 17+
```

### Step 3: Build the Application
```bash
mvn clean install
```

This will download all dependencies and build the application.

## ▶️ Running the Application

### Using Maven
```bash
mvn spring-boot:run
```

### Using JAR file (after building)
```bash
java -jar target/spring-boot-service-1.0.0.jar
```

The API will be available at `http://localhost:8080`

### Application Logs
When the application starts, you should see:
```
Started SpringBootServiceApplication in X.XXX seconds (process running for Y.YYY)
Tomcat started on port(s): 8080 (http)
```

## 🐳 Docker Setup

### Build Docker Image
```bash
docker build -t spring-boot-service:latest .
```

### Run Docker Container
```bash
docker run -p 8080:8080 spring-boot-service:latest
```

### Docker Compose (Optional)
If you have a `docker-compose.yml` file:
```bash
docker-compose up -d
```

### Verify Container is Running
```bash
docker ps
curl http://localhost:8080/hello
```

## ☸️ Kubernetes Deployment

### Prerequisites
- Minikube running and accessible
- kubectl configured
- Docker image built and pushed to registry (or available locally)

### Deploy to Minikube
```bash
kubectl create deployment spring-boot-service --image=spring-boot-service:latest
kubectl expose deployment spring-boot-service --port=8080 --target-port=8080 --type=LoadBalancer
```

### Check Deployment Status
```bash
kubectl get deployments
kubectl get pods
kubectl get services
```

### Port Forward to Access Service
```bash
kubectl port-forward service/spring-boot-service 8080:8080
```

### View Logs
```bash
kubectl logs deployment/spring-boot-service -f
```

## 📝 API Endpoints

### 1. Hello Endpoint
**GET** `/hello`

Returns a greeting message from Spring Boot.

**Response:**
```json
{
  "message": "Hello from Spring Boot"
}
```

**Example:**
```bash
curl http://localhost:8080/hello
```

### 2. Welcome Endpoint
**GET** `/`

Returns welcome message with service information.

**Response:**
```json
{
  "welcome": "Spring Boot Service",
  "version": "1.0.0",
  "endpoints": "/hello, /info"
}
```

**Example:**
```bash
curl http://localhost:8080/
```

### 3. Info Endpoint
**GET** `/info`

Returns application and system information.

**Response:**
```json
{
  "app_name": "Spring Boot Service",
  "version": "1.0.0",
  "java_version": "17.0.1",
  "os_name": "Linux"
}
```

**Example:**
```bash
curl http://localhost:8080/info
```

### 4. Health Check Endpoint
**GET** `/actuator/health`

Returns the health status of the service. Available through Spring Boot Actuator.

**Response:**
```json
{
  "status": "UP",
  "components": {
    "diskSpace": {...},
    "ping": {...}
  }
}
```

**Example:**
```bash
curl http://localhost:8080/actuator/health
```

## 🔧 Configuration

Configuration is managed through `application.properties` file located in `src/main/resources/`.

### Key Properties

| Property | Default | Description |
|----------|---------|-------------|
| `server.port` | `8080` | Port the server runs on |
| `spring.application.name` | `Spring Boot Service` | Application name |
| `logging.level.root` | `INFO` | Root logging level |
| `management.endpoints.web.exposure.include` | `health,info` | Exposed actuator endpoints |

### Changing Configuration
Edit `src/main/resources/application.properties`:
```properties
server.port=9000
logging.level.com.example.springboot=DEBUG
```

Or set via environment variables:
```bash
export SERVER_PORT=9000
mvn spring-boot:run
```

Or via command line:
```bash
mvn spring-boot:run -Dspring-boot.run.arguments="--server.port=9000"
```

## 🧪 Testing

### Using curl
```bash
# Test hello endpoint
curl http://localhost:8080/hello

# Test welcome endpoint
curl http://localhost:8080/

# Test info endpoint
curl http://localhost:8080/info

# Test health check
curl http://localhost:8080/actuator/health
```

### Using a Browser
Simply navigate to:
- `http://localhost:8080/hello`
- `http://localhost:8080/`
- `http://localhost:8080/info`

### Using Python
```python
import requests

# Test endpoints
response = requests.get("http://localhost:8080/hello")
print(response.json())

response = requests.get("http://localhost:8080/info")
print(response.json())
```

### Using PostMan
1. Create a new GET request
2. Enter URL: `http://localhost:8080/hello`
3. Click Send
4. View the JSON response

## 📂 Project Structure
```
SpringBootService/
├── pom.xml                                          # Maven configuration
├── src/
│   ├── main/
│   │   ├── java/com/example/springboot/
│   │   │   ├── SpringBootServiceApplication.java   # Main application class
│   │   │   └── controller/
│   │   │       └── HelloController.java             # REST controller
│   │   └── resources/
│   │       └── application.properties               # Application configuration
│   └── test/
│       └── java/com/example/springboot/
├── target/                                          # Compiled classes and JAR (after build)
├── Dockerfile                                       # Docker container configuration
├── .gitignore                                       # Git ignore file
└── README.md                                        # This file
```

## 🏗️ Building the Project

### Full Build
```bash
mvn clean install
```

### Skip Tests
```bash
mvn clean install -DskipTests
```

### Build only (no tests)
```bash
mvn clean package -DskipTests
```

The compiled JAR will be in `target/spring-boot-service-1.0.0.jar`

## 🔌 Integration with FastAPI Service

This Spring Boot service can be called by the FastAPI service using the `/call-java` endpoint. The FastAPI service makes a GET request to `http://spring-service:8080/hello`.

**Integration Example:**
1. FastAPI calls: `GET http://spring-service:8080/hello`
2. Spring Boot responds: `{"message": "Hello from Spring Boot"}`
3. FastAPI returns: `{"from_java": {"message": "Hello from Spring Boot"}}`

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Find and kill the process using port 8080
lsof -i :8080
kill -9 <PID>
```

### Build Issues
```bash
# Clear Maven cache
mvn clean

# Rebuild with verbose output
mvn clean install -X
```

### Java Version Issue
```bash
# Check Java version
java -version

# Should be Java 17 or higher
# If not, install Java 17 or set JAVA_HOME
```

### Application Won't Start
1. Check if port 8080 is available
2. Verify all dependencies are installed: `mvn dependency:resolve`
3. Check logs for error messages

### Docker Build Issues
```bash
# Build with no cache
docker build --no-cache -t spring-boot-service:latest .

# Check Docker logs
docker logs <container_id>
```

## 📊 Monitoring

### Health Check
```bash
curl http://localhost:8080/actuator/health
```

### Application Metrics
Enable additional metrics by adding to `application.properties`:
```properties
management.endpoints.web.exposure.include=health,info,metrics
```

Then access: `http://localhost:8080/actuator/metrics`

## 📜 License
See LICENSE file for details.

## 🤝 Contributing
Feel free to submit issues and enhancement requests!

## 📧 Support
For issues or questions, please contact me.
