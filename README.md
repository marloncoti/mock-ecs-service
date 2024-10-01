# Placeholder Web Server

This is a simple Python Flask-based web server meant to serve as a placeholder or template for deployments, especially in ECS or other container environments. It includes a basic `/healthcheck` route and allows dynamic port assignment via environment variables.

## Features

- **Flask-based web server**: A lightweight Python web server using Flask.
- **Dynamic port assignment**: The port on which the server listens is determined by the `APP_PORT` environment variable.
- **Healthcheck endpoint**: A `/healthcheck` route that returns a simple JSON response indicating the service is healthy.

## How to Use

### 1. Build the Docker Image

To build the Docker image, use the following command:

```bash
docker build -t placeholder-webserver .
```


### 2. Run the Container

When running the container, you can assign the listening port dynamically using the APP_PORT environment variable. For example, to run the container on port 8080:

```bash
docker run -e APP_PORT=8080 -p 8080:8080 placeholder-webserver
```