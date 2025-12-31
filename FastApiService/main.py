import os
import requests
from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Service",
    description="A simple FastAPI service that can call Java Spring Boot service",
    version="1.0.0"
)

SPRING_SERVICE_URL = os.getenv("SPRING_SERVICE_URL", "http://spring-service:8080")


@app.get("/hello")
def hello():
    """
    Simple endpoint that returns a greeting message.
    Returns:
        dict: A greeting message from FastAPI
    """
    return {"message": "Hello from FastAPI"}


@app.get("/call-java")
def call_java():
    """
    Endpoint that calls the Java Spring Boot service.
    Returns:
        dict: Response from the Java service or error message
    Raises:
        HTTPException: If the Spring service is unreachable
    """
    try:
        r = requests.get(f"{SPRING_SERVICE_URL}/hello", timeout=5)
        r.raise_for_status()
        return {"from_java": r.json()}
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to reach Spring service at {SPRING_SERVICE_URL}", "details": str(e)}


@app.get("/health")
def health_check():
    """
    Health check endpoint.
    Returns:
        dict: Status of the service
    """
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
