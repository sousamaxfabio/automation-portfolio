# Docker Foundations

A small Python HTTP service created to practise core Docker concepts: images, containers, Dockerfiles, port mapping, volumes, environment variables, and logs.

## What the application does

The service:

- Runs a Python web server inside a container
- Responds through `http://localhost:8080`
- Reads its message from an environment variable
- Stores a persistent visit count in a Docker volume
- Writes startup and HTTP request information to Docker logs

## Files

- `app.py` - Python HTTP service
- `Dockerfile` - Instructions for building the image
- `.dockerignore` - Files excluded from the Docker build context

## Build the image

```powershell
docker build -t day29-python:v4 .
```

## Run the container

```powershell
docker run -d --name day29-web -p 8080:8000 -v day29-data:/data -e APP_MESSAGE="Fabio's Docker service is running" day29-python:v4
```

Open `http://localhost:8080` in a browser.

## Inspect the container

```powershell
docker ps
docker logs day29-web
docker exec day29-web cat /data/visits.txt
```

## Stop and remove the container

```powershell
docker stop day29-web
docker rm day29-web
```

The `day29-data` volume remains available after the container is removed, so the visit count persists when a new container uses the same volume.
